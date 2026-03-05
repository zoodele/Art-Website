
document.addEventListener('DOMContentLoaded', () => {
    const filterButtons = document.querySelectorAll('.filters button');
    const galleryItems = document.querySelectorAll('.gallery-item');

    filterButtons.forEach(button => {
        button.addEventListener('click', () => {
            const filter = button.getAttribute('data-filter');
            galleryItems.forEach(item => {
                if (filter === 'all' || item.classList.contains(filter)) {
                    //item.style.display = '';
                    item.classList.remove('hide');
                } else {
                    //item.style.display = 'none';
                    item.classList.add('hide');
                }
            });
        });
    });
});
