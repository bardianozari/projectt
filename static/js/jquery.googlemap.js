    // مرکز نقشه: Kassel, Germany (نمونه)
    const center = [51.3127, 9.4797];

    // ایجاد نقشه
    const map = L.map('map').setView(center, 13);

    // لایه پس‌زمینه از OpenStreetMap
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 19,
      attribution: '&copy; OpenStreetMap contributors'
    }).addTo(map);

    // یک مارکر نمونه
    L.marker(center).addTo(map)
      .bindPopup('Hallo Kassel 👋')
      .openPopup();
