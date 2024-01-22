document.addEventListener('DOMContentLoaded', function() {
  
  // metrics
  var xValues = ["Luxary Cars", "Sport Cars", "Four-wheel Drive"];
  var yValues = [100, 49, 33];
  var barColors = [
    "#AB0552",
    "#B175FF",
    "#ffffff",
  ];

  new Chart("myChart", {
    type: "doughnut",
    data: {
      labels: xValues,
      datasets: [{
        backgroundColor: barColors,
        data: yValues
      }]
    },
    options: {
      title: {
        display: true,
        fontSize: 40,
        fontColor: '#ffffff',
        fontStyle: 'bold'
      },
      legend: {
        display: true,
        position: 'left', 
        align: 'center',
        labels: {
          fontColor: '#ffffffc7',
          usePointStyle: true,  // This line makes the legend items circular
          padding: 20
        }
      },
      animation: {
        duration: 2000,
      },
    }
});
  // car table
  const cars = [
    { model: 'Toyota Camry', color: 'Silver', brand: 'Toyota', category: 'Sedan', price: '$25,000' },
    { model: 'Honda Civic', color: 'Blue', brand: 'Honda', category: 'Sedan', price: '$22,000' },
    { model: 'Ford Mustang', color: 'Red', brand: 'Ford', category: 'Sport', price: '$35,000' },
    { model: 'Chevrolet Tahoe', color: 'Black', brand: 'Chevrolet', category: 'SUV', price: '$50,000' },
    { model: 'BMW 3 Series', color: 'White', brand: 'BMW', category: 'Luxury', price: '$40,000' },
    { model: 'Jeep Wrangler', color: 'Green', brand: 'Jeep', category: '4x4', price: '$45,000' },
    { model: 'Audi A4', color: 'Black', brand: 'Audi', category: 'Luxury', price: '$45,000' },
    { model: 'Tesla Model 3', color: 'Silver', brand: 'Tesla', category: 'Electric', price: '$50,000' },
    { model: 'Mercedes-Benz C-Class', color: 'Blue', brand: 'Mercedes-Benz', category: 'Luxury', price: '$50,000' },
    { model: 'Subaru Outback', color: 'Gray', brand: 'Subaru', category: 'SUV', price: '$35,000' },
    { model: 'Lamborghini Aventador', color: 'Yellow', brand: 'Lamborghini', category: 'Exotic', price: '$400,000' },
    { model: 'Porsche 911', color: 'Red', brand: 'Porsche', category: 'Sport', price: '$120,000' }
  ];

  const carTableBody = document.getElementById('carTableBody');
  const searchInput = document.getElementById('searchInput');

  function populateTable(cars) {
      carTableBody.innerHTML = '';

      cars.forEach(car => {
          const row = document.createElement('tr');

          row.innerHTML = `
              <td>${car.model}</td>
              <td>${car.color}</td>
              <td>${car.brand}</td>
              <td>${car.category}</td>
              <td>${car.price}</td>
          `;

          carTableBody.appendChild(row);
      });
  }

  populateTable(cars);

  searchInput.addEventListener('input', function() {
      const searchTerm = this.value.toLowerCase();

      const filteredCars = cars.filter(car => {
          return car.model.toLowerCase().includes(searchTerm) ||
                car.color.toLowerCase().includes(searchTerm) ||
                car.brand.toLowerCase().includes(searchTerm) ||
                car.category.toLowerCase().includes(searchTerm) ||
                car.price.toLowerCase().includes(searchTerm);
      });

      populateTable(filteredCars);
  });
});