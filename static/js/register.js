const app = Vue.createApp({
    data() {
        return {
            username: '',
            password: '',
            confirmPassword: ''
        };
    },
    methods: {
        async register() {
            if (this.password !== this.confirmPassword) {
                alert('As senhas não correspondem.');
                return;
            }
            try {
                const response = await fetch('/register', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        username: this.username,
                        password: this.password
                    }),
                });

                const data = await response.json();
                if (data.success) {
                    window.location.href = '/';
                } else {
                    alert('Erro no registro. Tente novamente.');
                }
            } catch (error) {
                console.error('Erro durante o registro:', error);
                alert('Erro ao tentar registrar.');
            }
        }
    }
});

app.mount('#app');
