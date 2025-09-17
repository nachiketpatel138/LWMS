// Slack-inspired UI functionality

// Mobile menu toggle
function toggleMobileMenu() {
    const overlay = document.getElementById('mobileMenuOverlay');
    const menu = document.getElementById('mobileMenu');
    
    if (overlay && menu) {
        overlay.classList.toggle('active');
        menu.classList.toggle('active');
    }
}

// Sidebar toggle for tablet/desktop
function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    if (sidebar) {
        sidebar.classList.toggle('collapsed');
    }
}

// Search functionality
function initializeSearch() {
    const searchInput = document.querySelector('.search-input');
    if (searchInput) {
        searchInput.addEventListener('input', function(e) {
            // Add search functionality here if needed
            console.log('Search:', e.target.value);
        });
    }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    initializeSearch();
    
    // Close mobile menu when clicking outside
    document.addEventListener('click', function(e) {
        const mobileMenu = document.getElementById('mobileMenu');
        const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
        const moreTab = document.querySelector('.nav-tab:last-child');
        
        if (mobileMenu && mobileMenu.classList.contains('active')) {
            if (!mobileMenu.contains(e.target) && 
                e.target !== mobileMenuBtn && 
                e.target !== moreTab &&
                !mobileMenuBtn.contains(e.target) &&
                !moreTab.contains(e.target)) {
                toggleMobileMenu();
            }
        }
    });
    
    // Auto-hide alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            if (alert.parentNode) {
                alert.classList.remove('show');
                setTimeout(() => {
                    if (alert.parentNode) {
                        alert.remove();
                    }
                }, 150);
            }
        }, 5000);
    });
});

// Utility functions for enhanced UX
function showNotification(message, type = 'info') {
    const container = document.querySelector('.messages-container') || 
                     document.querySelector('.main-content');
    
    if (container) {
        const alert = document.createElement('div');
        alert.className = `alert alert-${type} alert-dismissible fade show`;
        alert.innerHTML = `
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        `;
        
        if (document.querySelector('.messages-container')) {
            container.appendChild(alert);
        } else {
            container.insertBefore(alert, container.firstChild);
        }
        
        // Auto-hide after 5 seconds
        setTimeout(() => {
            if (alert.parentNode) {
                alert.classList.remove('show');
                setTimeout(() => {
                    if (alert.parentNode) {
                        alert.remove();
                    }
                }, 150);
            }
        }, 5000);
    }
}

// Enhanced table interactions
function initializeTableEnhancements() {
    const tables = document.querySelectorAll('.table');
    tables.forEach(table => {
        // Add hover effects to rows
        const rows = table.querySelectorAll('tbody tr');
        rows.forEach(row => {
            row.addEventListener('mouseenter', function() {
                this.style.backgroundColor = 'var(--bg-hover)';
            });
            row.addEventListener('mouseleave', function() {
                this.style.backgroundColor = '';
            });
        });
    });
}

// Initialize table enhancements when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    initializeTableEnhancements();
});