document.addEventListener('DOMContentLoaded', function() {
    const questionInput = document.getElementById('questionInput');
    const sendButton = document.getElementById('sendButton');
    const responseBox = document.getElementById('responseBox');

    // Function to simulate typing effect for responses
    function typeEffect(element, text, speed = 20) {
        element.innerHTML = ''; // Clear existing content
        let i = 0;
        element.classList.add('typing');
        
        function typing() {
            if (i < text.length) {
                element.innerHTML += text.charAt(i);
                i++;
                setTimeout(typing, speed);
            } else {
                element.classList.remove('typing');
                // Scroll to bottom of response box
                element.scrollTop = element.scrollHeight;
            }
        }
        
        typing();
    }

    // Function to send message and get response
    async function sendMessage() {
        const question = questionInput.value.trim();
        
        if (!question) {
            responseBox.innerHTML = '<span class="text-red-400">Error: Empty query detected. Please input data.</span>';
            return;
        }

        // Clear input
        questionInput.value = '';
        
        // Show loading state
        responseBox.innerHTML = '<span class="text-green-400 loading">Processing neural query</span>';
        
        try {
            const response = await fetch("/ask", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    question: question
                }),
            });

            if (!response.ok) {
                throw new Error(`Network response error: ${response.status}`);
            }

            const data = await response.json();
            
            if (data.error) {
                responseBox.innerHTML = `<span class="text-red-400">Error: ${data.error}</span>`;
            } else {
                // Apply typing effect to the response
                typeEffect(responseBox, data.response);
            }
        } catch (error) {
            console.error("Error:", error);
            responseBox.innerHTML = `<span class="text-red-400">Neural connection failure: ${error.message}</span>`;
        }
    }

    // Event listeners
    sendButton.addEventListener('click', sendMessage);
    
    questionInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });

    // Focus input on page load
    questionInput.focus();

    // Add scanner line effect on hover for the cyberpunk feel
    const card = document.querySelector('.cyberpunk-card');
    card.addEventListener('mousemove', function(e) {
        const scannerLine = document.createElement('div');
        scannerLine.style.position = 'absolute';
        scannerLine.style.width = '100%';
        scannerLine.style.height = '1px';
        scannerLine.style.background = 'linear-gradient(90deg, transparent, rgba(0, 255, 255, 0.8), transparent)';
        scannerLine.style.top = `${e.offsetY}px`;
        scannerLine.style.left = '0';
        scannerLine.style.pointerEvents = 'none';
        scannerLine.style.opacity = '0.5';
        scannerLine.style.zIndex = '100';
        
        this.appendChild(scannerLine);
        
        setTimeout(() => {
            scannerLine.remove();
        }, 300);
    });

    // Display welcome message with typing effect
    const welcomeMessage = "Neural interface online. Query database initialized. Awaiting input...";
    typeEffect(responseBox, welcomeMessage, 30);
});
