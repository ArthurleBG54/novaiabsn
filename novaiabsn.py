html_content_v2 = """<!DOCTYPE html>
<html lang="fr" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nova IA - L'Écosystème Business Ultime</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    colors: {
                        bgDark: '#06070B',
                        bgCard: '#0D0E16',
                        bgInput: '#131522',
                        brandBlue: '#1E40AF',
                        accentGroq: '#F59E0B',
                        accentClaude: '#CC7D6C',
                        accentManus: '#10B981',
                        borderColor: 'rgba(255, 255, 255, 0.06)'
                    }
                }
            }
        }
    </script>
    <style>
        /* Custom scrollbar matching Claude's UI */
        ::-webkit-scrollbar {
            width: 6px;
            height: 6px;
        }
        ::-webkit-scrollbar-track {
            background: transparent;
        }
        ::-webkit-scrollbar-thumb {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 9999px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: rgba(255, 255, 255, 0.2);
        }
        
        /* Smooth fade-in animation */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(8px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .animate-fade-in {
            animation: fadeIn 0.3s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        }

        /* Pulse animation for the Manus execution layer */
        @keyframes subtlePulse {
            0%, 100% { opacity: 0.15; }
            50% { opacity: 0.35; }
        }
        .manus-pulse {
            animation: subtlePulse 2s infinite ease-in-out;
        }
    </style>
</head>
<body class="bg-bgDark text-gray-100 font-sans antialiased h-screen overflow-hidden">

    <div class="flex h-full w-full">
        
        <aside class="w-64 bg-[#090A10] border-r border-borderColor flex flex-col justify-between shrink-0">
            <div>
                <div class="p-6 border-b border-borderColor flex items-center justify-between">
                    <span class="text-xl font-bold tracking-wider bg-gradient-to-r from-white via-gray-200 to-blue-500 bg-clip-text text-transparent">
                        Nova IA
                    </span>
                    <span class="text-[9px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-blue-900/40 text-blue-400 border border-blue-800/50">
                        BETA
                    </span>
                </div>
                
                <nav class="p-4 space-y-6">
                    <div>
                        <span class="text-[10px] font-semibold text-gray-500 uppercase tracking-widest block px-3 mb-2">Espace de Travail</span>
                        <div class="space-y-1">
                            <a href="#" id="link-chat" class="flex items-center space-x-3 px-3 py-2.5 rounded-xl bg-white/[0.04] text-white font-medium transition-all group">
                                <span class="w-2 h-2 rounded-full bg-blue-500 group-hover:scale-125 transition-transform"></span>
                                <span class="text-sm">Copilote de Bord</span>
                            </a>
                            <a href="#" id="link-pricing" class="flex items-center space-x-3 px-3 py-2.5 rounded-xl text-gray-400 hover:text-white hover:bg-white/[0.02] transition-all group">
                                <span class="w-2 h-2 rounded-full bg-transparent group-hover:bg-gray-500 transition-all"></span>
                                <span class="text-sm">Plans & Licences</span>
                            </a>
                        </div>
                    </div>

                    <div>
                        <span class="text-[10px] font-semibold text-gray-500 uppercase tracking-widest block px-3 mb-2">Projets Actifs</span>
                        <div class="space-y-1 text-xs text-gray-400">
                            <div class="px-3 py-2 rounded-lg hover:bg-white/[0.01] cursor-pointer truncate flex items-center justify-between">
                                <span>📈 Scaling Dropshipping</span>
                                <span class="text-[9px] bg-amber-500/10 text-amber-400 px-1.5 py-0.5 rounded">Groq</span>
                            </div>
                            <div class="px-3 py-2 rounded-lg hover:bg-white/[0.01] cursor-pointer truncate flex items-center justify-between">
                                <span>🛠️ Automatisation SaaS</span>
                                <span class="text-[9px] bg-emerald-500/10 text-emerald-400 px-1.5 py-0.5 rounded">Manus</span>
                            </div>
                        </div>
                    </div>
                </nav>
            </div>

            <div class="p-4 border-t border-borderColor bg-black/10">
                <div class="flex items-center justify-between">
                    <div class="flex items-center space-x-3">
                        <div class="w-8 h-8 rounded-full bg-gradient-to-tr from-blue-600 to-indigo-900 flex items-center justify-center text-xs font-bold text-white border border-white/10">
                            A
                        </div>
                        <div>
                            <p class="text-xs font-medium text-white">Arthur</p>
                            <p class="text-[10px] text-gray-500">Fondateur</p>
                        </div>
                    </div>
                    <span class="text-[9px] bg-gradient-to-r from-blue-600 to-indigo-600 text-white font-bold px-2 py-1 rounded border border-blue-400/20 shadow-lg shadow-blue-900/20">
                        PREMIUM
                    </span>
                </div>
            </div>
        </aside>

        <main class="flex-1 flex flex-col bg-bgDark relative h-full">
            
            <div id="wrapper-chat" class="flex flex-col h-full w-full">
                
                <header class="h-16 border-b border-borderColor flex items-center justify-between px-8 bg-bgDark/80 backdrop-blur-md z-10">
                    <div class="flex items-center space-x-4">
                        <span class="text-xs text-gray-400 font-medium">Moteur actif :</span>
                        <div class="bg-bgCard p-1 rounded-full border border-borderColor flex space-x-1 shadow-inner">
                            <button id="btn-groq" class="text-xs px-4 py-1.5 rounded-full font-medium transition-all duration-200 bg-accentGroq text-black shadow-md font-semibold" onclick="selectModel('groq')">
                                ⚡ Groq Llama
                            </button>
                            <button id="btn-claude" class="text-xs px-4 py-1.5 rounded-full font-medium transition-all duration-200 text-gray-400 hover:text-white" onclick="selectModel('claude')">
                                🧠 Claude 3.5
                            </button>
                            <button id="btn-manus" class="text-xs px-4 py-1.5 rounded-full font-medium transition-all duration-200 text-gray-400 hover:text-white" onclick="selectModel('manus')">
                                🤖 Manus Agent
                            </button>
                        </div>
                    </div>
                    <div class="text-xs text-gray-500 font-mono" id="model-status">Mode ultra-rapide activé</div>
                </header>

                <div class="flex-1 overflow-y-auto p-8 space-y-6" id="chat-messages-scroll">
                    
                    <div id="welcome-canvas" class="max-w-3xl mx-auto text-center my-12 animate-fade-in">
                        <h2 class="text-3xl font-extrabold tracking-tight text-white mb-3">
                            Lancez vos idées. Automatisez votre croissance.
                        </h2>
                        <p class="text-sm text-gray-400 max-w-xl mx-auto mb-10">
                            Basculez instantanément d'une IA à l'autre selon vos besoins du moment. Analyse stratégique ou exécution en arrière-plan.
                        </p>
                        
                        <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-left">
                            <div class="bg-bgCard border border-borderColor p-5 rounded-2xl hover:border-amber-500/20 hover:bg-white/[0.01] transition-all cursor-pointer group" onclick="selectModel('groq')">
                                <div class="w-8 h-8 rounded-lg bg-amber-500/10 flex items-center justify-center text-accentGroq font-bold text-sm mb-4 group-hover:scale-105 transition-transform">⚡</div>
                                <h3 class="text-white text-sm font-semibold mb-1">Groq Llama 3</h3>
                                <p class="text-gray-400 text-xs leading-relaxed">Vitesse de calcul absolue. Parfait pour générer des idées de business ou des scripts marketing à la volée.</p>
                            </div>
                            <div class="bg-bgCard border border-borderColor p-5 rounded-2xl hover:border-accentClaude/20 hover:bg-white/[0.01] transition-all cursor-pointer group" onclick="selectModel('claude')">
                                <div class="w-8 h-8 rounded-lg bg-[#CC7D6C]/10 flex items-center justify-center text-accentClaude font-bold text-sm mb-4 group-hover:scale-105 transition-transform">🧠</div>
                                <h3 class="text-white text-sm font-semibold mb-1">Claude 3.5 Sonnet</h3>
                                <p class="text-gray-400 text-xs leading-relaxed">Le cerveau stratégique. Analyse fine des structures financières, calculs de rentabilité et copywriting premium.</p>
                            </div>
                            <div class="bg-bgCard border border-borderColor p-5 rounded-2xl hover:border-emerald-500/20 hover:bg-white/[0.01] transition-all cursor-pointer group" onclick="selectModel('manus')">
                                <div class="w-8 h-8 rounded-lg bg-emerald-500/10 flex items-center justify-center text-accentManus font-bold text-sm mb-4 group-hover:scale-105 transition-transform">🤖</div>
                                <h3 class="text-white text-sm font-semibold mb-1">Manus Agent</h3>
                                <p class="text-gray-400 text-xs leading-relaxed">L'agent d'exécution autonome. Navigue sur le Web pour scrapper, analyser les concurrents et déployer des mini-sites.</p>
                            </div>
                        </div>
                    </div>

                    <div id="conversation-flow" class="max-w-3xl mx-auto space-y-6"></div>

                    <div id="ai-loader" class="max-w-3xl mx-auto flex items-start space-x-4 hidden">
                        <div class="w-7 h-7 rounded-lg bg-white/5 flex items-center justify-center border border-borderColor shrink-0">
                            <span class="text-xs" id="loader-icon">⚡</span>
                        </div>
                        <div class="bg-bgCard border border-borderColor px-4 py-3 rounded-2xl inline-flex space-x-1.5 items-center">
                            <div class="w-2 h-2 rounded-full bg-gray-500 animate-bounce" style="animation-delay: 0ms;"></div>
                            <div class="w-2 h-2 rounded-full bg-gray-500 animate-bounce" style="animation-delay: 150ms;"></div>
                            <div class="w-2 h-2 rounded-full bg-gray-500 animate-bounce" style="animation-delay: 300ms;"></div>
                        </div>
                    </div>

                </div>

                <footer class="p-6 bg-gradient-to-t from-bgDark via-bgDark to-transparent">
                    <div class="max-w-3xl mx-auto relative bg-bgInput border border-borderColor rounded-2xl p-2.5 focus-within:border-blue-600/50 focus-within:shadow-[0_0_20px_rgba(30,64,175,0.15)] transition-all flex flex-col">
                        <textarea id="chat-textarea" placeholder="Posez une question à l'IA ou confiez une mission autonome à l'agent..." class="bg-transparent text-sm text-white placeholder-gray-500 resize-none outline-none h-16 px-3 py-1 w-full"></textarea>
                        <div class="flex justify-between items-center px-2 pt-2 border-t border-white/[0.02]">
                            <span class="text-[10px] text-gray-500 font-mono">Shift + Entrée pour sauter une ligne</span>
                            <button id="btn-submit" class="bg-blue-600 hover:bg-blue-500 text-white rounded-xl px-4 py-2 text-xs font-semibold shadow-md shadow-blue-900/30 transition-all flex items-center space-x-2">
                                <span>Envoyer</span>
                                <span class="font-mono text-xs opacity-60">→</span>
                            </button>
                        </div>
                    </div>
                </footer>
            </div>

            <div id="wrapper-pricing" class="hidden flex-1 overflow-y-auto p-12 animate-fade-in">
                <div class="max-w-4xl mx-auto text-center mb-12">
                    <h2 class="text-3xl font-extrabold text-white tracking-tight mb-3">Une infrastructure taillée pour le scaling</h2>
                    <p class="text-sm text-gray-400">Passez d'un modèle d'IA à l'autre sans friction pour maximiser vos résultats.</p>
                </div>

                <div class="max-w-3xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-start">
                    <div class="bg-bgCard border border-borderColor rounded-3xl p-8 relative flex flex-col justify-between h-full hover:border-gray-700 transition-all">
                        <div>
                            <h3 class="text-lg font-bold text-white mb-1">Plan Fondateur</h3>
                            <p class="text-xs text-gray-500 mb-6">Pour valider vos premières idées de business.</p>
                            <div class="text-3xl font-extrabold text-white mb-6">0€ <span class="text-sm font-normal text-gray-500">/ mois</span></div>
                            
                            <ul class="space-y-3.5 text-xs text-gray-300 mb-8">
                                <li class="flex items-center space-x-2.5">
                                    <span class="text-emerald-500 font-bold">✓</span>
                                    <span>Modèle ultra-rapide <strong>Groq Llama 3</strong> inclus</span>
                                </li>
                                <li class="flex items-center space-x-2.5">
                                    <span class="text-emerald-500 font-bold">✓</span>
                                    <span>Génération d'idées et de stratégies basiques</span>
                                </li>
                                <li class="flex items-center space-x-2.5 text-gray-500 line-through">
                                    <span>✕</span>
                                    <span>Cerveau d'analyse premium Claude 3.5</span>
                                </li>
                                <li class="flex items-center space-x-2.5 text-gray-500 line-through">
                                    <span>✕</span>
                                    <span>Agent d'action autonome Manus</span>
                                </li>
                            </ul>
                        </div>
                        <button class="w-full bg-white/[0.04] text-gray-300 py-3 rounded-xl text-xs font-semibold hover:bg-white/[0.08] transition-all">
                            Votre formule active
                        </button>
                    </div>

                    <div class="bg-bgCard border-2 border-blue-600 rounded-3xl p-8 relative flex flex-col justify-between h-full shadow-[0_0_30px_rgba(30,64,175,0.15)]">
                        <span class="absolute -top-3 right-6 bg-blue-600 text-white text-[9px] font-bold uppercase tracking-wider px-3 py-1 rounded-full border border-blue-400/20">
                            PRO SCALE
                        </span>
                        <div>
                            <h3 class="text-lg font-bold text-white mb-1">Plan Elite Automate</h3>
                            <p class="text-xs text-blue-400 mb-6">L'arsenal complet pour déléguer et scaler.</p>
                            <div class="text-3xl font-extrabold text-white mb-6">49€ <span class="text-sm font-normal text-gray-500">/ mois</span></div>
                            
                            <ul class="space-y-3.5 text-xs text-gray-300 mb-8">
                                <li class="flex items-center space-x-2.5">
                                    <span class="text-blue-500 font-bold">✓</span>
                                    <span><strong>Groq Llama 3</strong> sans aucune limite de débit</span>
                                </li>
                                <li class="flex items-center space-x-2.5">
                                    <span class="text-blue-500 font-bold">✓</span>
                                    <span>Accès intégral à <strong>Claude 3.5 Sonnet</strong> (Stratégies avancées)</span>
                                </li>
                                <li class="flex items-center space-x-2.5">
                                    <span class="text-blue-500 font-bold">✓</span>
                                    <span>Accès à <strong>Manus Agent</strong> (Scrapping, Web, Déploiement d'apps)</span>
                                </li>
                                <li class="flex items-center space-x-2.5">
                                    <span class="text-blue-500 font-bold">✓</span>
                                    <span>Interconnexion de plateformes (Stripe, Shopify, Ad Networks)</span>
                                </li>
                            </ul>
                        </div>
                        <button class="w-full bg-blue-600 text-white py-3 rounded-xl text-xs font-semibold hover:bg-blue-500 transition-all shadow-md shadow-blue-900/30">
                            Rejoindre l'Élite
                        </button>
                    </div>
                </div>
            </div>

        </main>
    </div>

    <script>
        // Sélection des éléments DOM fondamentaux
        const linkChat = document.getElementById('link-chat');
        const linkPricing = document.getElementById('link-pricing');
        const wrapperChat = document.getElementById('wrapper-chat');
        const wrapperPricing = document.getElementById('wrapper-pricing');
        
        const chatTextarea = document.getElementById('chat-textarea');
        const btnSubmit = document.getElementById('btn-submit');
        const conversationFlow = document.getElementById('conversation-flow');
        const welcomeCanvas = document.getElementById('welcome-canvas');
        const aiLoader = document.getElementById('ai-loader');
        const chatMessagesScroll = document.getElementById('chat-messages-scroll');
        const modelStatusText = document.getElementById('model-status');
        const loaderIcon = document.getElementById('loader-icon');

        // Modèle courant global
        let activeModel = 'groq';

        // Routage de la navigation
        linkChat.addEventListener('click', (e) => {
            e.preventDefault();
            toggleTabs(linkChat, linkPricing, wrapperChat, wrapperPricing);
        });

        linkPricing.addEventListener('click', (e) => {
            e.preventDefault();
            toggleTabs(linkPricing, linkChat, wrapperPricing, wrapperChat);
        });

        function toggleTabs(activeLink, inactiveLink, activeWrapper, inactiveWrapper) {
            inactiveLink.classList.remove('bg-white/[0.04]', 'text-white', 'font-medium');
            inactiveLink.classList.add('text-gray-400', 'hover:text-white', 'hover:bg-white/[0.02]');
            inactiveLink.querySelector('span').className = 'w-2 h-2 rounded-full bg-transparent group-hover:bg-gray-500 transition-all';
            
            activeLink.classList.remove('text-gray-400', 'hover:text-white', 'hover:bg-white/[0.02]');
            activeLink.classList.add('bg-white/[0.04]', 'text-white', 'font-medium');
            activeLink.querySelector('span').className = 'w-2 h-2 rounded-full bg-blue-500 group-hover:scale-125 transition-transform';

            inactiveWrapper.classList.add('hidden');
            activeWrapper.classList.remove('hidden');
        }

        // Changement dynamique de modèle IA
        function selectModel(model) {
            activeModel = model;
            const bGroq = document.getElementById('btn-groq');
            const bClaude = document.getElementById('btn-claude');
            const bManus = document.getElementById('btn-manus');

            // Reset styles
            [bGroq, bClaude, bManus].forEach(btn => {
                btn.className = 'text-xs px-4 py-1.5 rounded-full font-medium transition-all duration-200 text-gray-400 hover:text-white';
            });

            if(model === 'groq') {
                bGroq.className = 'text-xs px-4 py-1.5 rounded-full font-semibold transition-all duration-200 bg-accentGroq text-black shadow-md shadow-amber-500/10';
                modelStatusText.innerText = 'Mode ultra-rapide activé';
                loaderIcon.innerText = '⚡';
            } else if(model === 'claude') {
                bClaude.className = 'text-xs px-4 py-1.5 rounded-full font-semibold transition-all duration-200 bg-accentClaude text-white shadow-md shadow-[#CC7D6C]/10';
                modelStatusText.innerText = 'Logique de calcul avancée activée';
                loaderIcon.innerText = '🧠';
            } else if(model === 'manus') {
                bManus.className = 'text-xs px-4 py-1.5 rounded-full font-semibold transition-all duration-200 bg-accentManus text-white shadow-md shadow-emerald-500/10';
                modelStatusText.innerText = 'Agent d\'exécution web autonome armé';
                loaderIcon.innerText = '🤖';
            }
        }

        // Moteur de discussion et rendu HTML des blocs de messages
        function buildMessageNode(sender, text, modelUsed = '') {
            const block = document.createElement('div');
            block.className = `flex space-x-4 animate-fade-in ${sender === 'user' ? 'justify-end' : 'justify-start'}`;

            let avatarMarkup = '';
            let contentStyle = '';

            if (sender === 'user') {
                avatarMarkup = `
                    <div class="w-7 h-7 rounded-lg bg-blue-600/20 text-blue-400 font-bold border border-blue-500/30 text-xs flex items-center justify-center order-2 ml-4 shrink-0 shadow-sm">U</div>
                `;
                contentStyle = 'bg-blue-600 text-white border border-blue-500/20 rounded-2xl rounded-tr-none px-4 py-3 text-sm max-w-xl shadow-md shadow-blue-900/10';
            } else {
                let badgeColor = 'bg-amber-500/10 text-accentGroq border-amber-500/20';
                let icon = '⚡';
                if(modelUsed === 'claude') { badgeColor = 'bg-[#CC7D6C]/10 text-accentClaude border-[#CC7D6C]/20'; icon = '🧠'; }
                if(modelUsed === 'manus') { badgeColor = 'bg-emerald-500/10 text-accentManus border-emerald-500/20'; icon = '🤖'; }

                avatarMarkup = `
                    <div class="w-7 h-7 rounded-lg bg-white/5 border border-borderColor text-xs flex items-center justify-center mr-4 shrink-0 shadow-sm">${icon}</div>
                `;
                contentStyle = 'bg-bgCard border border-borderColor text-gray-200 rounded-2xl rounded-tl-none px-4 py-3 text-sm max-w-xl shadow-sm relative';
            }

            const textContainer = document.createElement('div');
            textContainer.className = contentStyle;
            
            // Gestion des sous-badges informatifs pour le backend simulé
            if(sender === 'assistant') {
                const badge = document.createElement('div');
                badge.className = `text-[9px] uppercase tracking-wider font-bold mb-1.5 px-1.5 py-0.5 rounded border w-fit ${modelUsed === 'groq' ? 'bg-amber-500/10 text-accentGroq border-amber-500/20' : modelUsed === 'claude' ? 'bg-[#CC7D6C]/10 text-accentClaude border-[#CC7D6C]/20' : 'bg-emerald-500/10 text-accentManus border-emerald-500/20'}`;
                badge.innerText = modelUsed;
                textContainer.appendChild(badge);
            }

            const innerText = document.createElement('p');
            innerText.className = 'leading-relaxed whitespace-pre-wrap';
            innerText.innerText = text;
            textContainer.appendChild(innerText);

            block.innerHTML = avatarMarkup;
            if (sender === 'user') {
                block.insertBefore(textContainer, block.firstChild);
            } else {
                block.appendChild(textContainer);
            }

            return block;
        }

        // Simulation de la couche de prompt de réponse IA selon le cas de figure
        function computeIntelligenceOutput(model, prompt) {
            const userPrompt = prompt.toLowerCase();
            
            if (model === 'groq') {
                return "Voici une exécution instantanée sur la base de votre requête Llama 3 :\n\nPour valider rapidement ce levier, lancez une campagne d'acquisition micro-budget (5€/jour) ciblée sur votre niche pour collecter de la data brute en moins de 24h. C'est le moyen le plus efficace d'obtenir des métriques claires sans gaspiller vos ressources.";
            } else if (model === 'claude') {
                return "Analyse stratégique de structure business (Claude 3.5 Sonnet) :\n\nPour construire une croissance saine (Scaling), nous devons disséquer vos indicateurs fondamentaux :\n1. Optimisation du Tunnel de Conversion : Alignement du copywriting sur les points de friction de votre avatar client.\n2. Équilibre unitaire (LTV / CAC) : Votre valeur de vie client doit impérativement représenter au minimum le triple de votre coût d'acquisition.\n\nRecommandation : Avant d'augmenter vos budgets publicitaires, déployez une séquence d'emailing de rétention automatisée pour maximiser la rentabilité de votre trafic existant.";
            } else {
                return "[ACTION PROTOCOLE MANUS] Déploiement d'un agent autonome initié dans l'environnement virtuel cloud.\n\nActions entreprises :\n- Initialisation du moteur de navigation headless pour analyser les 5 concurrents majeurs de votre secteur.\n- Extraction des structures tarifaires, des pages de vente et des scripts d'intégration publicitaire.\n- Génération automatique d'un rapport de synthèse structuré et d'une structure de landing page optimisée pour votre projet.\n\nLe script tourne en tâche de fond. Un rapport complet avec les fichiers de code épurés sera mis à votre disposition dans votre espace de stockage d'ici quelques instants.";
            }
        }

        // Déclencheur d'envoi du message
        function performMessageDispatch() {
            const rawText = chatTextarea.value.trim();
            if (!rawText) return;

            // Masquage de l'écran d'accueil lors de l'initialisation de l'échange
            welcomeCanvas.classList.add('hidden');

            // Intégration du bloc utilisateur
            const userNode = buildMessageNode('user', rawText);
            conversationFlow.appendChild(userNode);
            chatTextarea.value = '';

            // Affichage du module de chargement
            aiLoader.classList.remove('hidden');
            chatMessagesScroll.scrollTop = chatMessagesScroll.scrollHeight;

            // Modélisation du temps de calcul asynchrone des réseaux de neurones (1.4s)
            setTimeout(() => {
                aiLoader.classList.add('hidden');
                
                const aiOutput = computeIntelligenceOutput(activeModel, rawText);
                const assistantNode = buildMessageNode('assistant', aiOutput, activeModel);
                
                conversationFlow.appendChild(assistantNode);
                chatMessagesScroll.scrollTop = chatMessagesScroll.scrollHeight;
            }, 1400);
        }

        // Événements d'envoi (Bouton et Touche Entrée)
        btnSubmit.addEventListener('click', performMessageDispatch);
        chatTextarea.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                performMessageDispatch();
            }
        });
    </script>
</body>
</html>
"""

with open("Nova_IA_Ecosystem.html", "w", encoding="utf-8") as f:
    f.write(html_content_v2)
print("Nova IA file generated.")
