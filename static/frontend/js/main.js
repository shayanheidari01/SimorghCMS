// Main JavaScript functions
document.addEventListener('DOMContentLoaded', function() {
    // Initialize components
    initializeComponents();
    
    // Load posts on posts page
    if (document.getElementById('postsContainer')) {
        loadPosts();
    }
    
    // Load post detail
    if (document.getElementById('postDetail')) {
        const urlParams = new URLSearchParams(window.location.search);
        const postId = urlParams.get('id');
        if (postId) {
            loadPostDetail(postId);
        }
    }
});

// Initialize components
function initializeComponents() {
    // Add click events to dropdowns
    const dropdowns = document.querySelectorAll('.dropdown');
    dropdowns.forEach(dropdown => {
        const btn = dropdown.querySelector('.dropdown-btn');
        const content = dropdown.querySelector('.dropdown-content');
        
        btn.addEventListener('click', function(e) {
            e.stopPropagation();
            content.style.display = content.style.display === 'block' ? 'none' : 'block';
        });
    });
    
    // Close dropdowns when clicking outside
    document.addEventListener('click', function() {
        document.querySelectorAll('.dropdown-content').forEach(content => {
            content.style.display = 'none';
        });
    });
}

// Load posts for posts page
async function loadPosts() {
    const container = document.getElementById('postsContainer');
    const pagination = document.getElementById('pagination');
    
    if (!container) return;
    
    try {
        utils.showLoading(container);
        
        const posts = await api.getPosts();
        
        if (posts.length === 0) {
            container.innerHTML = `
                <div class="text-center" style="grid-column: 1 / -1;">
                    <p>مقاله‌ای یافت نشد.</p>
                </div>
            `;
            return;
        }
        
        container.innerHTML = posts.map(post => `
            <div class="post-card">
                <div class="post-image">
                    ${post.featured_image ? 
                        `<img src="${post.featured_image}" alt="${post.title}" style="width:100%;height:100%;object-fit:cover;">` : 
                        'تصویر مقاله'
                    }
                </div>
                <div class="post-content">
                    <h3 class="post-title">
                        <a href="/post?id=${post.id}">${post.title}</a>
                    </h3>
                    <p class="post-excerpt">${post.excerpt || 'بدون خلاصه'}</p>
                    <div class="post-meta">
                        <span class="post-author">${post.author?.username || 'ناشناس'}</span>
                        <span class="post-date">${utils.formatDate(post.created_at)}</span>
                    </div>
                </div>
            </div>
        `).join('');
        
    } catch (error) {
        utils.hideLoading(container);
        utils.showAlert('خطا در بارگذاری مقالات: ' + error.message, 'error');
    }
}

// Load post detail
async function loadPostDetail(postId) {
    const container = document.getElementById('postDetail');
    
    if (!container) return;
    
    try {
        utils.showLoading(container);
        
        const post = await api.getPost(postId);
        
        container.innerHTML = `
            <article class="post-detail">
                <header class="post-header">
                    <h1 class="post-detail-title">${post.title}</h1>
                    <div class="post-detail-meta">
                        <span>نویسنده: ${post.author?.username || 'ناشناس'}</span>
                        <span>تاریخ: ${utils.formatDate(post.created_at)}</span>
                        <span>وضعیت: ${post.status === 'published' ? 'منتشر شده' : 'پیش‌نویس'}</span>
                    </div>
                </header>
                <div class="post-body">
                    ${post.content || '<p>بدون محتوا</p>'}
                </div>
            </article>
        `;
        
    } catch (error) {
        utils.hideLoading(container);
        utils.showAlert('خطا در بارگذاری مقاله: ' + error.message, 'error');
        container.innerHTML = '<p class="text-center">مقاله یافت نشد.</p>';
    }
}

// Load user profile
async function loadUserProfile() {
    const container = document.getElementById('profileContainer');
    
    if (!container) return;
    
    if (!auth.isLoggedIn()) {
        window.location.href = '/login';
        return;
    }
    
    try {
        utils.showLoading(container);
        
        const user = await auth.getUser();
        
        if (user) {
            container.innerHTML = `
                <div class="form-container">
                    <h2 class="form-title">پروفایل کاربری</h2>
                    <div class="form-group">
                        <label class="form-label">نام کاربری</label>
                        <input type="text" class="form-input" value="${user.username}" readonly>
                    </div>
                    <div class="form-group">
                        <label class="form-label">ایمیل</label>
                        <input type="email" class="form-input" value="${user.email}" readonly>
                    </div>
                    <div class="form-group">
                        <label class="form-label">نام</label>
                        <input type="text" class="form-input" value="${user.first_name || ''}" readonly>
                    </div>
                    <div class="form-group">
                        <label class="form-label">نام خانوادگی</label>
                        <input type="text" class="form-input" value="${user.last_name || ''}" readonly>
                    </div>
                    <div class="form-group">
                        <label class="form-label">نقش</label>
                        <input type="text" class="form-input" value="${user.role}" readonly>
                    </div>
                    <div class="form-group">
                        <label class="form-label">تاریخ عضویت</label>
                        <input type="text" class="form-input" value="${utils.formatDate(user.created_at)}" readonly>
                    </div>
                </div>
            `;
        }
        
    } catch (error) {
        utils.hideLoading(container);
        utils.showAlert('خطا در بارگذاری پروفایل: ' + error.message, 'error');
    }
}

// Load dashboard
async function loadDashboard() {
    const container = document.getElementById('dashboardContainer');
    
    if (!container) return;
    
    if (!auth.isLoggedIn()) {
        window.location.href = '/login';
        return;
    }
    
    try {
        utils.showLoading(container);
        
        const user = await auth.getUser();
        const posts = await api.getPosts(0, 5); // Get last 5 posts
        
        if (user) {
            container.innerHTML = `
                <div class="container">
                    <h2 class="page-title">داشبورد</h2>
                    
                    <div class="mb-4">
                        <h3>خوش آمدید، ${user.username}!</h3>
                        <p>نقش شما: ${user.role}</p>
                    </div>
                    
                    <div class="mb-4">
                        <h3>آخرین مقالات شما</h3>
                        <div id="userPosts" class="posts-grid">
                            ${posts.length > 0 ? 
                                posts.slice(0, 3).map(post => `
                                    <div class="post-card">
                                        <div class="post-content">
                                            <h4 class="post-title">${post.title}</h4>
                                            <p class="post-excerpt">${post.excerpt || 'بدون خلاصه'}</p>
                                            <div class="post-meta">
                                                <span>${utils.formatDate(post.created_at)}</span>
                                                <span>${post.status === 'published' ? 'منتشر شده' : 'پیش‌نویس'}</span>
                                            </div>
                                        </div>
                                    </div>
                                `).join('') :
                                '<p>مقاله‌ای یافت نشد.</p>'
                            }
                        </div>
                    </div>
                    
                    <div class="form-actions">
                        <a href="create-/post" class="btn btn-primary">ایجاد مقاله جدید</a>
                        <a href="/profile" class="btn btn-outline">مشاهده پروفایل</a>
                    </div>
                </div>
            `;
        }
        
    } catch (error) {
        utils.hideLoading(container);
        utils.showAlert('خطا در بارگذاری داشبورد: ' + error.message, 'error');
    }
}

// Export functions
window.loadPosts = loadPosts;
window.loadPostDetail = loadPostDetail;
window.loadUserProfile = loadUserProfile;
window.loadDashboard = loadDashboard;