
$().ready(function () {
$("#dynamic-alert").click(function() {
            swal.queue([{
                title: "Your public IP",
                confirmButtonColor: "#5664d2",
                confirmButtonText: "Show my public IP",
                text: "Your public IP will be received via AJAX request",
                showLoaderOnConfirm: !0,
                preConfirm: function() {
                    return new Promise(function(e) {
                        t.get("https://api.ipify.org?format=json").done(function(t) {
                            swal.insertQueueStep(t.ip), e()
                        })
                    })
                }
            }])
  
    });
});



