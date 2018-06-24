window.onload = () => {

    if(localStorage.getItem('SERVER_IP') && localStorage.getItem('SERVER_PORT')){ //Verifica se já tem IP e PORTA salvos no navegador, se tiver
        firebase.auth().onAuthStateChanged((user) => {
            if(!user) location.href="index.html";
            return;
        });


        document.getElementById('getTemperatura').addEventListener('click', (e) => {
            fetch(`http://${localStorage.getItem('SERVER_IP')}:${localStorage.getItem('SERVER_PORT')}/temp`).then(res => {
                res.json().then(result => {
                    document.getElementById('dado').innerHTML = "<span class='tag is-success is-medium'>Temperatura: "+result.temperatura+"</span>";
                })
            }, err => {
                alert("Ocorreu um erro na requisição!");
            });
        });

        document.getElementById('getAgua').addEventListener('click', (e) => {
            fetch(`http://${localStorage.getItem('SERVER_IP')}:${localStorage.getItem('SERVER_PORT')}/agua`).then(res => {
                res.json().then(result => {
                    document.getElementById('dado').innerHTML = "<span class='tag is-success is-medium'>Nível da água: "+result.agua+"</span>";
                })
            }, err => {
                alert("Ocorreu um erro na requisição!");
            });
        });

    }else{
        firebase.auth().signOut().then(res => {
            location.href="index.html";
            return;
        }, err => {
            alert(err);
        });
    }
}

load = () => {
    fetch('http://localhost:5000/dados').then(res => {
        res.json().then(result => {
            document.getElementById('textoTemperatura').innerHTML = "temp: "+result.temperatura+"°C";
            document.getElementById('textoAgua').innerHTML = "agua: "+result.agua;
        })
    }, err => {
        alert("Ocorreu um erro na requisição!");
    });
};
