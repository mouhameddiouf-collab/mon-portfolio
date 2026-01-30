document.addEventListener("DOMContentLoaded", function() {

    /* =========================================
       0. GESTION DU LOADER (CRITIQUE 🚨)
       C'est ce qui manquait pour enlever l'écran de chargement !
       ========================================= */
    const loader = document.getElementById('loader-wrapper');
    
    // Fonction pour cacher le loader et afficher le site
    function hideLoader() {
        if (loader) {
            loader.style.transition = 'opacity 0.5s ease';
            loader.style.opacity = '0'; // On le rend transparent
            
            setTimeout(() => {
                loader.style.display = 'none'; // On le supprime
                document.body.classList.add('loaded'); // On affiche le site
            }, 500);
        } else {
            // Sécurité si le loader n'existe pas
            document.body.classList.add('loaded');
        }
    }

    // On attend que TOUT soit chargé (images incluses) ou un délai max
    window.addEventListener('load', hideLoader);
    // Sécurité : Si le chargement est trop long, on force l'affichage après 3 secondes
    setTimeout(hideLoader, 3000);


    /* =========================================
       1. FLUIDITÉ & TRANSITIONS (Fade Out au clic)
       ========================================= */
    const links = document.querySelectorAll('a');
    links.forEach(link => {
        if (link.hostname === window.location.hostname && !link.hash && link.target !== "_blank") {
            link.addEventListener('click', e => {
                e.preventDefault();
                const targetUrl = link.href;
                document.body.classList.remove('loaded'); 
                setTimeout(() => {
                    window.location.href = targetUrl;
                }, 500); 
            });
        }
    });

    /* =========================================
       2. GESTION DU MODE NUIT
       ========================================= */
    const toggleSwitch = document.querySelector('#checkbox');
    const currentTheme = localStorage.getItem('theme');

    if (currentTheme) {
        document.body.classList.add(currentTheme);
        if (currentTheme === 'dark-mode' && toggleSwitch) {
            toggleSwitch.checked = true;
        }
    }

    if (toggleSwitch) {
        toggleSwitch.addEventListener('change', function(e) {
            if (e.target.checked) {
                document.body.classList.add('dark-mode');
                localStorage.setItem('theme', 'dark-mode');
            } else {
                document.body.classList.remove('dark-mode');
                localStorage.setItem('theme', 'light');
            }
        });
    }

    /* =========================================
       3. MENU ACTIF
       ========================================= */
    const currentLocation = location.href;
    const menuItem = document.querySelectorAll('nav ul li a');
    menuItem.forEach(item => {
        if (item.href === currentLocation) {
            item.classList.add('active');
        }
    });

    /* =========================================
       4. INITIALISATION DES ANIMATIONS
       ========================================= */
    if (typeof AOS !== 'undefined') {
        AOS.init({
            duration: 800,
            easing: 'ease-out-cubic',
            once: true,
            offset: 50,
        });
    }

    if (document.querySelector('.typed-text') && typeof Typed !== 'undefined') {
        new Typed('.typed-text', {
            strings: ["Géographe", "Aspirant Data Analyst", "Cartographe", "Passionné d'Environnement"],
            typeSpeed: 50,
            backSpeed: 30,
            backDelay: 2000,
            loop: true
        });
    }

    /* =========================================
       5. MENU MOBILE
       ========================================= */
    const menuToggle = document.getElementById('mobile-menu');
    const navMenu = document.querySelector('nav ul');
    if (menuToggle && navMenu) {
        menuToggle.addEventListener('click', () => {
            menuToggle.classList.toggle('is-active');
            navMenu.classList.toggle('active');
        });
    }

    /* =========================================
       6. PARTICULES DE FOND
       ========================================= */
    const canvas = document.getElementById('geo-canvas');
    if (canvas) {
        const ctx = canvas.getContext('2d');
        let particlesArray;
        
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        
        let mouse = { x: null, y: null, radius: (canvas.height/80) * (canvas.width/80) };
        
        window.addEventListener('mousemove', function(event) {
            mouse.x = event.x;
            mouse.y = event.y;
        });

        class Particle {
            constructor(x, y, directionX, directionY, size, color) {
                this.x = x; this.y = y;
                this.directionX = directionX; this.directionY = directionY;
                this.size = size; this.color = color;
            }
            draw() {
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2, false);
                ctx.fillStyle = '#0ca789';
                ctx.fill();
            }
            update() {
                if (this.x > canvas.width || this.x < 0) this.directionX = -this.directionX;
                if (this.y > canvas.height || this.y < 0) this.directionY = -this.directionY;
                
                let dx = mouse.x - this.x;
                let dy = mouse.y - this.y;
                let distance = Math.sqrt(dx*dx + dy*dy);
                if (distance < mouse.radius + this.size) {
                    if (mouse.x < this.x && this.x < canvas.width - this.size * 10) this.x += 3;
                    if (mouse.x > this.x && this.x > this.size * 10) this.x -= 3;
                    if (mouse.y < this.y && this.y < canvas.height - this.size * 10) this.y += 3;
                    if (mouse.y > this.y && this.y > this.size * 10) this.y -= 3;
                }
                this.x += this.directionX;
                this.y += this.directionY;
                this.draw();
            }
        }

        function init() {
            particlesArray = [];
            let numberOfParticles = (canvas.height * canvas.width) / 9000;
            for (let i = 0; i < numberOfParticles; i++) {
                let size = (Math.random() * 2) + 1;
                let x = (Math.random() * ((innerWidth - size * 2) - (size * 2)) + size * 2);
                let y = (Math.random() * ((innerHeight - size * 2) - (size * 2)) + size * 2);
                let directionX = (Math.random() * 2) - 1;
                let directionY = (Math.random() * 2) - 1;
                particlesArray.push(new Particle(x, y, directionX, directionY, size, '#0ca789'));
            }
        }

        function animate() {
            requestAnimationFrame(animate);
            ctx.clearRect(0,0,innerWidth, innerHeight);
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
                    if (distance < (canvas.width/7) * (canvas.height/7)) {
                        opacityValue = 1 - (distance/20000);
                        ctx.strokeStyle = 'rgba(12, 167, 137,' + opacityValue + ')';
                        ctx.lineWidth = 1;
                        ctx.beginPath();
                        ctx.moveTo(particlesArray[a].x, particlesArray[a].y);
                        ctx.lineTo(particlesArray[b].x, particlesArray[b].y);
                        ctx.stroke();
                    }
                }
            }
        }
        
        window.addEventListener('resize', function() {
            canvas.width = innerWidth;
            canvas.height = innerHeight;
            init();
        });

        init();
        animate();
    }

    /* =========================================
       7. CARTE LEAFLET
       ========================================= */
    if (document.getElementById('ma-carte') && typeof L !== 'undefined') {
        delete L.Icon.Default.prototype._getIconUrl;
        L.Icon.Default.mergeOptions({
            iconRetinaUrl: 'https://unpkg.com/leaflet@1.7.1/dist/images/marker-icon-2x.png',
            iconUrl: 'https://unpkg.com/leaflet@1.7.1/dist/images/marker-icon.png',
            shadowUrl: 'https://unpkg.com/leaflet@1.7.1/dist/images/marker-shadow.png',
        });

        var map = L.map('ma-carte').setView([14.7167, -17.4677], 13);
        L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; OpenStreetMap contributors'
        }).addTo(map);

        const scriptData = document.getElementById('lieux-data');
        if (scriptData) {
             try {
                const lieux = JSON.parse(scriptData.textContent);
                lieux.forEach(lieu => {
                    L.marker([lieu.latitude, lieu.longitude]).addTo(map)
                     .bindPopup(`<b>${lieu.nom}</b><br>${lieu.description}`);
                });
             } catch(e) { console.log("Pas de lieux chargés"); }
        } else {
             L.marker([14.7167, -17.4677]).addTo(map).bindPopup('<b>Dakar</b>').openPopup();
        }
    }
});

// MAGIC CURSOR SCRIPT
const cursorDot = document.querySelector('.cursor-dot');
const cursorOutline = document.querySelector('.cursor-outline');

window.addEventListener('mousemove', function(e) {
    const posX = e.clientX;
    const posY = e.clientY;

    // Le point suit instantanément
    cursorDot.style.left = `${posX}px`;
    cursorDot.style.top = `${posY}px`;

    // Le cercle suit avec un délai (animation fluide)
    cursorOutline.animate({
        left: `${posX}px`,
        top: `${posY}px`
    }, { duration: 500, fill: "forwards" });
});

// Effet quand on survole un lien
const interactiveElements = document.querySelectorAll('a, button, .btn, .card');
interactiveElements.forEach(el => {
    el.addEventListener('mouseenter', () => document.body.classList.add('hovering'));
    el.addEventListener('mouseleave', () => document.body.classList.remove('hovering'));
});

/* =========================================
   MENU MOBILE INTERACTIF
   ========================================= */
document.addEventListener('DOMContentLoaded', function() {
    const menuToggle = document.querySelector('.menu-toggle');
    const navMenu = document.querySelector('nav ul');
    const navLinks = document.querySelectorAll('nav ul li a');

    if (menuToggle) {
        menuToggle.addEventListener('click', () => {
            // Ouvre/Ferme le menu
            navMenu.classList.toggle('active');
            // Change l'icône (ajoute la classe active au bouton aussi)
            menuToggle.classList.toggle('active');
            
            // Animation en cascade des liens (Effet Whaou)
            navLinks.forEach((link, index) => {
                if (link.style.animation) {
                    link.style.animation = '';
                } else {
                    link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 0.3}s`;
                }
            });
        });
    }

    // Fermer le menu quand on clique sur un lien
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            navMenu.classList.remove('active');
            menuToggle.classList.remove('active');
        });
    });
});