document.addEventListener('DOMContentLoaded', () => {

    // 1. Mobile Menu Toggle
    const btn = document.getElementById('mobile-menu-btn');
    const menu = document.getElementById('mobile-menu');

    if (btn && menu) {
        btn.addEventListener('click', () => {
            menu.classList.toggle('hidden');
        });
    }

    // 2. Scroll Animation (IntersectionObserver)
    const reveals = document.querySelectorAll('.reveal');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
            }
        });
    }, { threshold: 0.1 });

    reveals.forEach(el => observer.observe(el));

    // 3. Typewriter Effect (Only if element exists)
    const typeTarget = document.getElementById('typewriter');
    if (typeTarget) {
        const words = ["Network Architect", "Malware Analyst", "Security Researcher"];
        let i = 0;
        let timer;

        function typeWriter() {
            const word = words[i];
            const currentText = typeTarget.textContent;

            if (!this.isDeleting && currentText !== word) {
                typeTarget.textContent = word.substring(0, currentText.length + 1);
            } else if (this.isDeleting && currentText !== "") {
                typeTarget.textContent = word.substring(0, currentText.length - 1);
            }

            let typeSpeed = 100;
            if (this.isDeleting) typeSpeed /= 2;

            if (!this.isDeleting && currentText === word) {
                typeSpeed = 2000;
                this.isDeleting = true;
            } else if (this.isDeleting && currentText === "") {
                this.isDeleting = false;
                i = (i + 1) % words.length;
                typeSpeed = 500;
            }
            timer = setTimeout(typeWriter, typeSpeed);
        }
        typeWriter();
    }

    // 4. Network Constellation Canvas Effect (Only if canvas exists)
    const canvas = document.getElementById('network-canvas');
    if (canvas) {
        const ctx = canvas.getContext('2d');
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;

        let particlesArray;

        class Particle {
            constructor() {
                this.x = Math.random() * canvas.width;
                this.y = Math.random() * canvas.height;
                this.directionX = (Math.random() * 0.4) - 0.2;
                this.directionY = (Math.random() * 0.4) - 0.2;
                this.size = Math.random() * 2;
                this.color = '#0ea5e9'; // Accent Cyan
            }
            draw() {
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2, false);
                ctx.fillStyle = this.color;
                ctx.fill();
            }
            update() {
                if (this.x > canvas.width || this.x < 0) this.directionX = -this.directionX;
                if (this.y > canvas.height || this.y < 0) this.directionY = -this.directionY;
                this.x += this.directionX;
                this.y += this.directionY;
                this.draw();
            }
        }

        function init() {
            particlesArray = [];
            let numberOfParticles = (canvas.height * canvas.width) / 9000;
            for (let i = 0; i < numberOfParticles; i++) {
                particlesArray.push(new Particle());
            }
        }

        function animate() {
            requestAnimationFrame(animate);
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            for (let i = 0; i < particlesArray.length; i++) {
                particlesArray[i].update();
            }
            connect();
        }

        function connect() {
            let opacityValue = 1;
            for (let a = 0; a < particlesArray.length; a++) {
                for (let b = a; b < particlesArray.length; b++) {
                    let distance = ((particlesArray[a].x - particlesArray[b].x) * (particlesArray[a].x - particlesArray[b].x)) + ((particlesArray[a].y - particlesArray[b].y) * (particlesArray[a].y - particlesArray[b].y));
                    if (distance < (canvas.width / 7) * (canvas.height / 7)) {
                        opacityValue = 1 - (distance / 20000);
                        ctx.strokeStyle = 'rgba(14, 165, 233,' + opacityValue + ')';
                        ctx.lineWidth = 1;
                        ctx.beginPath();
                        ctx.moveTo(particlesArray[a].x, particlesArray[a].y);
                        ctx.lineTo(particlesArray[b].x, particlesArray[b].y);
                        ctx.stroke();
                    }
                }
            }
        }

        window.addEventListener('resize', () => {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
            init();
        });

        init();
        animate();
    }

    // 5. Card Mouse Tracking Glow
    const handleOnMouseMove = e => {
        const { currentTarget: target } = e;
        const rect = target.getBoundingClientRect(),
            x = e.clientX - rect.left,
            y = e.clientY - rect.top;

        target.style.setProperty("--mouse-x", `${x}px`);
        target.style.setProperty("--mouse-y", `${y}px`);
    }

    for (const card of document.querySelectorAll(".devhub-card")) {
        card.onmousemove = e => handleOnMouseMove(e);
    }

    // 6. Scroll Progress Bar
    const progressContainer = document.querySelector('body');
    const progressBar = document.createElement('div');
    progressBar.id = 'scroll-progress';
    document.body.prepend(progressBar);

    window.addEventListener('scroll', () => {
        const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
        const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        const scrolled = (winScroll / height) * 100;
        document.getElementById("scroll-progress").style.width = scrolled + "%";
    });

    // 7. Live Intelligence Feed Simulator
    const feed = document.getElementById('live-feed');
    if (feed) {
        const messages = [
            "INITIALIZING_VULN_SCAN...",
            "DB_SHARD_ESTABLISHED [0.0.1]",
            "TCP_HANDSHAKE: 10.0.4.12:443 -> ACCEPTED",
            "RECOGNIZING_IDENTITY_VECTORS...",
            "PARSING_SECURITY_TRANSCRIPT...",
            "ENCRYPTING_LOCAL_STORAGE...",
            "BYPASSING_RESTRICTIONS_LEVEL_4...",
            "SUCCESS: ARCHIVE_SYNC_COMPLETE"
        ];
        let msgIndex = 0;

        function updateFeed() {
            const span = document.createElement('span');
            span.className = 'block opacity-0 translate-x-[-10px] transition-all duration-500 text-[10px] text-accent-cyan mb-1';
            span.textContent = `[${new Date().toLocaleTimeString()}] ${messages[msgIndex]}`;

            feed.appendChild(span);
            if (feed.children.length > 5) feed.removeChild(feed.firstChild);

            // Trigger animation
            setTimeout(() => {
                span.classList.remove('opacity-0', 'translate-x-[-10px]');
            }, 10);

            msgIndex = (msgIndex + 1) % messages.length;
            setTimeout(updateFeed, Math.random() * 2000 + 1000);
        }
        updateFeed();
    }
    // 8. Copy to Clipboard for Code Blocks (Universal Observer)
    const addCopyButton = (pre) => {
        // Prevent duplicate buttons
        if (pre.querySelector('.copy-btn-injected')) return;

        // Create button
        const btn = document.createElement('button');
        btn.innerHTML = '<i class="fa-regular fa-copy"></i>';
        btn.className = 'copy-btn-injected absolute top-2 right-2 text-slate-400 hover:text-white transition-all duration-200 opacity-0 group-hover:opacity-100 p-2 rounded bg-slate-800/50 backdrop-blur-sm border border-slate-700/50';
        btn.setAttribute('aria-label', 'Copy to clipboard');

        // Make pre relative for positioning and group for hover
        pre.classList.add('relative', 'group');
        pre.appendChild(btn);

        btn.addEventListener('click', () => {
            const code = pre.querySelector('code');
            // Remove the LAST newline character if it exists, as pre tags often have an extra one
            let text = code ? code.innerText : pre.innerText;

            navigator.clipboard.writeText(text).then(() => {
                // Button Feedback
                const originalIcon = btn.innerHTML;
                btn.innerHTML = '<i class="fa-solid fa-check text-green-400"></i>';

                // Visual Highlight Feedback (Flash Green)
                // Use !important to override any specific CSS rules
                const originalTransition = pre.style.transition;
                pre.style.transition = 'background-color 0.2s';
                pre.style.setProperty('background-color', 'rgba(34, 197, 94, 0.15)', 'important');

                setTimeout(() => {
                    btn.innerHTML = originalIcon;
                    pre.style.setProperty('background-color', '', ''); // Reset to default
                    // Restore transition after cleanup to avoid getting stuck
                    setTimeout(() => { pre.style.transition = originalTransition; }, 200);
                }, 1000);
            }).catch(err => {
                console.error('Failed to copy:', err);
                btn.innerHTML = '<i class="fa-solid fa-xmark text-red-500"></i>';
            });
        });
    };

    // Initial Run
    document.querySelectorAll('pre').forEach(addCopyButton);

    // Watch for new content (MutationObserver)
    const copyObserver = new MutationObserver((mutations) => {
        mutations.forEach((mutation) => {
            mutation.addedNodes.forEach((node) => {
                if (node.nodeType === 1) { // Element node
                    if (node.tagName === 'PRE') {
                        addCopyButton(node);
                    } else if (node.querySelectorAll) {
                        node.querySelectorAll('pre').forEach(addCopyButton);
                    }
                }
            });
        });
    });

    copyObserver.observe(document.body, {
        childList: true,
        subtree: true
    });

});
