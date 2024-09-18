const app = Vue.createApp({
    data() {
        return {
            username: '',
            password: ''
        };
    },
    methods: {
        async login() {
            try {
                const response = await fetch('/login', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        username: this.username,
                        password: this.password,
                    }),
                });

                if (!response.ok) {
                    throw new Error('Erro na requisição: ' + response.statusText);
                }

                const data = await response.json();

                if (data.success) {
                    window.location.href = '/home';
                } else {
                    alert('Login falhou');
                }
            } catch (error) {
                console.error('Erro durante o login:', error);
                alert('Erro ao realizar login. Verifique suas credenciais ou tente novamente mais tarde.');
            }
        }
    }
});

app.mount('#app');
