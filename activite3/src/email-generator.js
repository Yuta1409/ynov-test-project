function generateEmailConfirmation(userInfo) {
    const { name, email, registration } = userInfo;
    return `
        Bonjour ${name},
        Merci de vous être inscrit le ${registration} avec l'adresse email ${email}.
    `;
}

module.exports = { generateEmailConfirmation };