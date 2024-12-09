const apiEndpoint = 'YOUR_API_GATEWAY_URL';

document.getElementById('bookingForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const name = document.getElementById('name').value;
    const unitType = document.getElementById('unitType').value;
    const startDate = document.getElementById('startDate').value;

    const response = await fetch(`${apiEndpoint}/bookings`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            booking_id: Date.now().toString(),
            customer_name: name,
            unit_type: unitType,
            start_date: startDate,
        }),
    });

    const data = await response.json();
    alert(data.message);
});
