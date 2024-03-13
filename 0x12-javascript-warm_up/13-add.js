#!/usr/bin/node
// Define the function
function add(a, b) {
    return a + b;
}

// Export the function for Node.js
if (typeof module !== 'undefined' && module.exports) {
    module.exports = add;
}

// Export the function for browser environment
if (typeof window !== 'undefined') {
    window.add = add;
}
