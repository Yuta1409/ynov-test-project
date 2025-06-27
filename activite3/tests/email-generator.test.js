const { generateEmailConfirmation } = require('../src/email-generator.js');

describe('Generation d\'email', () => {

    it('Générer une confirmation d\'email avec les info de l\'utilisateur', () => {
        const userInfo = {
            name: 'Jean Dupont',
            email: 'jean.dupont@example.com',
            registration: '2023-10-01'
        };

    const expectedEmail = `
        Bonjour ${userInfo.name},
        Merci de vous être inscrit le ${userInfo.registration} avec l'adresse email ${userInfo.email}.
    `;

    const emailOutput = generateEmailConfirmation(userInfo);
    expect(emailOutput).toBe(expectedEmail);
    });
});