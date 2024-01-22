// Function to show the cookie consent popup
function showCookieConsent() {
    const cookieConsent = document.getElementById('cookieConsent');
    cookieConsent.style.display = 'block';
}

// Function to hide the cookie consent popup and set a cookie
function acceptCookies() {
    const cookieConsent = document.getElementById('cookieConsent');
    cookieConsent.style.display = 'none';

    // Set a cookie to remember user's choice
    document.cookie = 'cookieConsent=true; max-age=' + (365 * 24 * 60 * 60) + '; path=/';
}

// Check if the user has already accepted cookies
function checkCookieConsent() {
    const cookies = document.cookie;
    if (!cookies.includes('cookieConsent=true')) {
        showCookieConsent();
    }
}

// Check for cookie consent on page load
window.onload = checkCookieConsent;