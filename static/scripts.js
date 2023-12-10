

let sidebarOpen = false;
const sidebar = document.getElementById('sidebar');

function openSidebar() {
  if (!sidebarOpen) {
    sidebar.classList.add('sidebar-responsive');
    sidebarOpen = true;
  }
}

function closeSidebar() {
  if (sidebarOpen) {
    sidebar.classList.remove('sidebar-responsive');
    sidebarOpen = false;
  }
}

// ---------- CHARTS ----------

// BAR CHART
const barChartOptions = {
  series: [
    {
      data: [10, 8, 6, 4, 2],
    },
  ],
  chart: {
    type: 'bar',
    height: 350,
    toolbar: {
      show: false,
    },
  },
  colors: ['#246dec', '#cc3c43', '#367952', '#f5b74f', '#4f35a1'],
  plotOptions: {
    bar: {
      distributed: true,
      borderRadius: 4,
      horizontal: false,
      columnWidth: '40%',
    },
  },
  dataLabels: {
    enabled: false,
  },
  legend: {
    show: false,
  },
  xaxis: {
    categories: ['Laptop', 'Phone', 'Monitor', 'Headphones', 'Camera'],
  },
  yaxis: {
    title: {
      text: 'Count',
    },
  },
};

const barChart = new ApexCharts(
  document.querySelector('#bar-chart'),
  barChartOptions
);
barChart.render();

// AREA CHART
const areaChartOptions = {
  series: [
    {
      name: 'Purchase Orders',
      data: [31, 40, 28, 51, 42, 109, 100],
    },
    {
      name: 'Sales Orders',
      data: [11, 32, 45, 32, 34, 52, 41],
    },
  ],
  chart: {
    height: 350,
    type: 'area',
    toolbar: {
      show: false,
    },
  },
  colors: ['#4f35a1', '#246dec'],
  dataLabels: {
    enabled: false,
  },
  stroke: {
    curve: 'smooth',
  },
  labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'],
  markers: {
    size: 0,
  },
  yaxis: [
    {
      title: {
        text: 'Purchase Orders',
      },
    },
    {
      opposite: true,
      title: {
        text: 'Sales Orders',
      },
    },
  ],
  tooltip: {
    shared: true,
    intersect: false,
  },
};

const areaChart = new ApexCharts(
  document.querySelector('#area-chart'),
  areaChartOptions
);
areaChart.render();


// Lista de gastos
const expenseList = document.getElementById('expense-list');
const searchExpenseInput = document.getElementById('search-expense');
const filterDateInput = document.getElementById('filter-date');

// Função para adicionar um gasto à lista
function addExpenseToList(name, description, value, date) {
  const li = document.createElement('li');
  li.innerHTML = `<strong>${name}</strong> - ${description} - R$ ${value.toFixed(2)} - ${new Date(date).toLocaleString()}`;
  expenseList.appendChild(li);
}

// Função para filtrar gastos por nome
function searchExpense() {
  const searchValue = searchExpenseInput.value.toLowerCase();
  const expenses = document.querySelectorAll('#expense-list li');

  expenses.forEach((expense) => {
    const expenseName = expense.textContent.toLowerCase();
    expense.style.display = expenseName.includes(searchValue) ? 'block' : 'none';
  });
}

// Função para filtrar gastos por data
function filterByDate() {
  const filterDateValue = filterDateInput.value;
  const expenses = document.querySelectorAll('#expense-list li');

  expenses.forEach((expense) => {
    const expenseDate = new Date(expense.textContent.split('-').pop().trim()).toLocaleDateString();
    expense.style.display = expenseDate === filterDateValue ? 'block' : 'none';
  });
}

// Adiciona eventos aos elementos
searchExpenseInput.addEventListener('input', searchExpense);
filterDateInput.addEventListener('input', filterByDate);

// ... Seu código existente ...