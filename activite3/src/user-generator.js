function createUser(userInfo) {
    const { name, email, password } = userInfo;
    // Logic to create a new user
    return {
        id: generateUniqueId(),
        name,
        email,
        passwordHash: hashPassword(password)
    };
}

function generateUniqueId() {
    return Math.random().toString(36).substr(2, 9);
}

function hashPassword(password) {
    return 'hashed_' + password;
}

module.exports = { createUser };