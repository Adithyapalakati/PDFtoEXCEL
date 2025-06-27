function updateCell(input) {
  const row = input.dataset.row;
  const col = input.dataset.col;
  const value = input.value;

  fetch("/update", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ row, col, value })
  }).then(res => res.json())
    .then(data => {
      if (!data.success) alert("Failed to update");
    });
}

function exportExcel() {
  fetch("/export")
    .then(res => res.json())
    .then(data => {
      const link = document.createElement("a");
      link.href = data.download;
      link.download = "sheet.xlsx";
      link.click();
    });
}


function collectTables() {
    const tables = document.querySelectorAll('.editable-table');
    const allTablesData = [];

    tables.forEach(table => {
      const headers = Array.from(table.querySelectorAll('thead input')).map(input => input.value.trim());
      const rows = Array.from(table.querySelectorAll('tbody tr')).map(row => {
        return Array.from(row.querySelectorAll('td input')).map(input => input.value.trim());
      });

      const df = {
        columns: headers,
        rows: rows
      };

      allTablesData.push(df);
    });

    document.getElementById('table_data').value = JSON.stringify(allTablesData);
    return true;
  }