const { createUser } = require('../src/user-generator.js');

describe('User Registration', () => {
    it('should create a new user with valid information', () => {
        const userInfo = {
            name: 'Alice Smith',
            email: 'alice.smith@example.com',
            password: 'securepassword'
        };
        const newUser = createUser(userInfo);
        expect(newUser).toHaveProperty('id');
        expect(newUser.name).toBe(userInfo.name);
        expect(newUser.email).toBe(userInfo.email);
        expect(newUser.passwordHash).toBeDefined(); // Assuming password is hashed
    });
});