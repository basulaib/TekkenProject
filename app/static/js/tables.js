$(document).ready( function () {
    $('#t').DataTable(
        {
            dom: 'Bfrtip',
            buttons: [
                {
                    extend: 'colvis',
                    text: 'Column invis'
                }
            ],
            colReorder: true,
            paging: true,
            scroller: true,
            scrollY: 1000,
            fixedHeader: true,
            colReorder: {
                realtime: false
            }
        }
    );
} );