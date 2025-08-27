const toggleBtn = document.getElementById('toggleBtn');
const cancelBtn = document.getElementById('cancelBtn');
const sidebar = document.getElementById('sidebar');

toggleBtn.addEventListener('click', () => {
    sidebar.classList.add('active');
});

cancelBtn.addEventListener('click', () => {
    sidebar.classList.remove('active');
});
