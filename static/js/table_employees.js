let dataTable;
let dataTableIsInitialized = false;
var editButtons = document.querySelectorAll('.edit-button');
editButtons.forEach(function (button) {
    button.addEventListener('click', function () {
        var id = this.getAttribute('data-id');
        // Haz algo con el 'id', como redirigir a la página de editar
        window.location.href = '/edit_employee/' + id; // Cambiar 'edit_employee' según tu ruta
    });
});

const dataTableOptions = {
    columnDefs: [
        { className: "cole", targets: [0, 1, 2, 3] },
        { orderable: false, targets: [3] },
    ],
    destroy: true,
    language: {
        lengthMenu: "Mostrando _MENU_ registros por página",
        zeroRecords: "No se encontraron empleados",
        info: "Mostrando desde _START_ hasta _END_ de un total de _TOTAL_ registros",
        infoEmpty: "No se encontraron empleados",
        infoFiltered: "(filtrado del total de _MAX_ registros)",
        search: "Buscar:",
        loadingRecords: "Cargando...",
        paginate: {
            first: "Primero",
            last: "Último",
            next: "Siguiente",
            previous: "Anterior"
        }
    }
};

const initDataTable = async () => {
    if (dataTableIsInitialized) {
        dataTable.destroy();
    }
    await listEmployees(); // Cambiar a la función que obtiene la lista de empleados
    dataTable = $('#employee_datatable').DataTable(dataTableOptions); // Cambiar 'employee_datatable' según tu tabla
    dataTableIsInitialized = true;
};

const listEmployees = async () => {
    try {
        const response = await fetch('http://127.0.0.1:8000/list_employee/'); // Cambiar la URL según tu API
        const contentType = response.headers.get("content-type");
        if (contentType && contentType.includes("application/json")) {
            const data = await response.json();
            let content = ``;
            data.employees.forEach(employee => {
                content += `<tr>

                                <td>${employee.id}</td>
                                <td>${employee.firstname}</td>
                                <td>${employee.lastname}</td>
                                <td>${employee.documentnumber}</td>
                                <td>${employee.idsubarea.namesubarea}</td>
                                <td>${employee.idsubarea.idarea.namearea}</td>
                                

                                <td>
                                    <a href="/edit_employee/${employee.id}" type="button" class="btn btn-primary">Actualizar</a>
                                    <button type="button" class="btn btn-danger" data-bs-toggle="modal" data-bs-target="#staticBackdrop">Eliminar</button>
                                </td>
                            </tr>`;
            });
            document.getElementById('employee_table_body').innerHTML = content; // Cambiar 'employee_table_body' según tu tabla body
        } else {
            console.error("La respuesta no es JSON.");
        }
    } catch (ex) {
        console.error("Error al procesar la respuesta:", ex);
    }
};

window.addEventListener('load', async() => {
    await initDataTable();
});
