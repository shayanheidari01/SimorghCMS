// برای حالت تولید - آدرس نسبی
const API_BASE_URL = '/api/v1';

// API Functions
const api = {
    // Auth endpoints
    async login(username, password) {
        const response = await fetch(`${API_BASE_URL}/auth/login`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: new URLSearchParams({
                username: username,
                password: password
            })
        });
        
        if (!response.ok) {
            throw new Error('ورود ناموفق بود');
        }
        
        return await response.json();
    },

    async register(userData) {
        const response = await fetch(`${API_BASE_URL}/auth/register`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(userData)
        });
        
        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || 'ثبت نام ناموفق بود');
        }
        
        return await response.json();
    },

    // User endpoints
    async getCurrentUser(token) {
        const response = await fetch(`${API_BASE_URL}/users/me`, {
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json',
            }
        });
        
        if (!response.ok) {
            throw new Error('خطا در دریافت اطلاعات کاربر');
        }
        
        return await response.json();
    },

    // Posts endpoints
    async getPosts(skip = 0, limit = 10) {
        const response = await fetch(`${API_BASE_URL}/posts?skip=${skip}&limit=${limit}`);
        
        if (!response.ok) {
            throw new Error('خطا در دریافت مقالات');
        }
        
        return await response.json();
    },

    async getPost(id) {
        const response = await fetch(`${API_BASE_URL}/posts/${id}`);
        
        if (!response.ok) {
            throw new Error('مقاله یافت نشد');
        }
        
        return await response.json();
    },

    async createPost(postData, token) {
        const response = await fetch(`${API_BASE_URL}/posts`, {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(postData)
        });
        
        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || 'خطا در ایجاد مقاله');
        }
        
        return await response.json();
    },

    async updatePost(id, postData, token) {
        const response = await fetch(`${API_BASE_URL}/posts/${id}`, {
            method: 'PUT',
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(postData)
        });
        
        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || 'خطا در ویرایش مقاله');
        }
        
        return await response.json();
    },

    async deletePost(id, token) {
        const response = await fetch(`${API_BASE_URL}/posts/${id}`, {
            method: 'DELETE',
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json',
            }
        });
        
        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || 'خطا در حذف مقاله');
        }
        
        return await response.json();
    }
};

// Utility functions
const utils = {
    formatDate(dateString) {
        const options = { 
            year: 'numeric', 
            month: 'long', 
            day: 'numeric',
            hour: '2-digit',
            minute: '2-digit'
        };
        return new Date(dateString).toLocaleDateString('fa-IR', options);
    },

    showAlert(message, type = 'info') {
        // Remove existing alerts
        const existingAlert = document.querySelector('.alert');
        if (existingAlert) {
            existingAlert.remove();
        }

        const alert = document.createElement('div');
        alert.className = `alert alert-${type}`;
        alert.textContent = message;

        // Insert at the beginning of the container
        const container = document.querySelector('.container') || document.body;
        container.insertBefore(alert, container.firstChild);

        // Auto remove after 5 seconds
        setTimeout(() => {
            if (alert.parentNode) {
                alert.remove();
            }
        }, 5000);
    },

    showLoading(element) {
        element.innerHTML = '<div class="spinner"></div>';
    },

    hideLoading(element) {
        element.innerHTML = '';
    }
};

// Export
window.api = api;
window.utils = utils;