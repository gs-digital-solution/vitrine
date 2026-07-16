// JavaScript personnalisé (vous pouvez ajouter des animations ou effets plus tard)
console.log("Site Vitrine - Prêt !");

// Exemple : Fermer automatiquement les alertes après 5 secondes
document.addEventListener('DOMContentLoaded', function() {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.transition = 'opacity 0.5s';
            alert.style.opacity = '0';
            setTimeout(() => alert.remove(), 500);
        }, 5000);
    });
});