window.onload = () => { //Ao carregar a página executa o bloco
    if(!localStorage.getItem('SERVER_IP') && !localStorage.getItem('SERVER_PORT')){ //Verifica se já tem IP e PORTA salvos no navegador, senão tiver:
        document.getElementById('loading').style.display = 'none'; //Tira o elemento de carregando
        document.getElementById('setServerDetails').style.display = 'block'; //Exibe o formulário para preencher o IP e PORTA
        document.getElementById('setUserLogin').style.display = 'none'; //Não exibe o formulário de login

        document.getElementById('setIpAndPort').addEventListener('click', (e) => {
            const ip   = document.getElementById('inputIp').value;
            const port = document.getElementById('inputPort').value;
        
            if(ip == '' || port == ''){
                alert("Preencha todos os campos!");
            }else{
                localStorage.setItem("SERVER_IP", ip);
                localStorage.setItem("SERVER_PORT", port);
                location.reload();
            }
        });
    }else{
        document.getElementById('loading').style.display = 'none'; //Tira o elemento de carregando
        document.getElementById('setServerDetails').style.display = 'none'; //Não exibe o formulário para preencher o IP e PORTA
        document.getElementById('setUserLogin').style.display = 'block'; //Exibe o formulário de login

        document.querySelectorAll('#actionBtn').forEach(e => {
            e.addEventListener('click', (elem) => {
                const email    = document.getElementById('email').value;
                const password = document.getElementById('password').value;

                console.log(email)

                if(email == '' || password == ''){
                    alert("Preencha todos os campos!");
                }else{
                    switch (elem.target.getAttribute("name")) {
                        case "login":
                            firebase.auth().signInWithEmailAndPassword(email, password).then(res => {
                                alert("Logado com sucesso!");
                                location.href="console.html";
                            }, err => {
                                alert(err);
                            });  
                        break;
                    
                        default:
                            firebase.auth().createUserWithEmailAndPassword(email, password).then(res => {
                                alert("Usuário criado com sucesso!");
                                location.href="console.html";
                            }, err => {
                                alert(err);
                            });
                        break;
                    }                    
                }
            });
        });
        
        firebase.auth().onAuthStateChanged((user) => {
            if(user) location.href="console.html";
            return;
        });
    }
};
