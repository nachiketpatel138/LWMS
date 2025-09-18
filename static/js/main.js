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



// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
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