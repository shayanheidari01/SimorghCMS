// Authentication functions
const auth = {
    // Check if user is logged in
    isLoggedIn() {
        return !!localStorage.getItem('token');
    },

    // Get user token
    getToken() {
        return localStorage.getItem('token');
    },

    // Get user info
    async getUser() {
        const token = this.getToken();
        if (!token) return null;

        try {
            const user = await api.getCurrentUser(token);
            return user;
        } catch (error) {
            console.error('Error getting user:', error);
            this.logout();
            return null;
        }
    },

    // Login user
    async login(username, password) {
        try {
            const data = await api.login(username, password);
            localStorage.setItem('token', data.access_token);
            return data;
        } catch (error) {
            throw error;
        }
    },

    // Register user
    async register(userData) {
        try {
            const data = await api.register(userData);
            return data;
        } catch (error) {
            throw error;
        }
    },

    // Logout user
    logout() {
        localStorage.removeItem('token');
        window.location.href = '/';
    },

    // Update UI based on auth status
    updateAuthUI() {
        const authButtons = document.getElementById('authButtons');
        const userMenu = document.getElementById('userMenu');
        const usernameSpan = document.getElementById('username');

        if (this.isLoggedIn()) {
            authButtons.style.display = 'none';
            userMenu.style.display = 'flex';
            
            // Load user info
            this.getUser().then(user => {
                if (user) {
                    usernameSpan.textContent = user.username;
                }
            });
        } else {
            authButtons.style.display = 'flex';
            userMenu.style.display = 'none';
        }
    }
};

// Initialize auth on page load
document.addEventListener('DOMContentLoaded', function() {
    // Update auth UI
    auth.updateAuthUI();

    // Setup logout button
    const logoutBtn = document.getElementById('logoutBtn');
    if (logoutBtn) {
        logoutBtn.addEventListener('click', function(e) {
            e.preventDefault();
            auth.logout();
        });
    }

    // Setup login form
    const loginForm = document.getElementById('loginForm');
    if (loginForm) {
        loginForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;
            const submitBtn = document.getElementById('loginSubmit');
            const originalText = submitBtn.innerHTML;

            try {
                submitBtn.innerHTML = '<div class="spinner"></div> در حال ورود...';
                submitBtn.disabled = true;

                await auth.login(username, password);
                utils.showAlert('ورود موفقیت‌آمیز بود!', 'success');
                
                // Redirect to dashboard
                setTimeout(() => {
                    window.location.href = '/dashboard';
                }, 1000);
                
            } catch (error) {
                utils.showAlert(error.message || 'خطا در ورود', 'error');
                submitBtn.innerHTML = originalText;
                submitBtn.disabled = false;
            }
        });
    }

    // Setup register form
    const registerForm = document.getElementById('registerForm');
    if (registerForm) {
        registerForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const formData = new FormData(registerForm);
            const userData = {
                username: formData.get('username'),
                email: formData.get('email'),
                password: formData.get('password'),
                first_name: formData.get('first_name') || '',
                last_name: formData.get('last_name') || ''
            };

            const submitBtn = document.getElementById('registerSubmit');
            const originalText = submitBtn.innerHTML;

            try {
                submitBtn.innerHTML = '<div class="spinner"></div> در حال ثبت نام...';
                submitBtn.disabled = true;

                await auth.register(userData);
                utils.showAlert('ثبت نام موفقیت‌آمیز بود! اکنون می‌توانید وارد شوید.', 'success');
                
                // Clear form
                registerForm.reset();
                
                // Redirect to login
                setTimeout(() => {
                    window.location.href = '/login';
                }, 2000);
                
            } catch (error) {
                utils.showAlert(error.message || 'خطا در ثبت نام', 'error');
                submitBtn.innerHTML = originalText;
                submitBtn.disabled = false;
            }
        });
    }
});

// Export auth
window.auth = auth;