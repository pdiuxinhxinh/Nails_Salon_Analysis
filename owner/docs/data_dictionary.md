# Data Dictionary: Booking Records

This dataset contains appointment booking records from a nail salon. Each row represents a service included in a booking, providing information about the appointment date, booking details, client, service, assigned staff member, pricing, and appointment duration.

| Column | Data Type | Description | Example |
|---|---|---|---|
| `date` | Date | Date when the appointment was created or recorded. | 2026-10-31 |
| `created_by` | Categorical | Indicates whether the booking was created by the business or the client. | Business, Client |
| `number` | Integer / Identifier | Unique booking or appointment reference number used to identify related service records. | 9882567 |
| `phone_number` | String | Client's contact phone number. Partially masked to protect personal information. | +1519884xxxx |
| `status` | Categorical | Current or final status of the appointment. | Completed, Cancel |
| `client_name` | String / Identifier | Name or anonymized identifier of the client who booked the appointment. | M, E, A |
| `service_name` | Categorical | Name of the nail service requested by the client. | MANI & PEDI, BIO GEL REFILL |
| `staff_name` | Categorical | Name of the staff member assigned to perform the service. | Quinie, Victoria, Daisy |
| `service_price` | Numeric (Currency) | Price charged or listed for the individual service. | 50, 45, 40 |
| `start_time` | Time | Scheduled starting time of the service. | 09:30 |
| `end_time` | Time | Scheduled ending time of the service. | 10:45 |

## Additional Notes

- **Record granularity:** Each row represents an individual service within a booking. A single booking number may appear across multiple rows when a client requests multiple services.
- **Booking identification:** The `number` column can be used to group services belonging to the same booking.
- **Data privacy:** Phone numbers are masked, and client names are represented by abbreviated identifiers to protect customer privacy.
- **Appointment duration:** Duration can be calculated by subtracting `start_time` from `end_time`.
- **Service revenue:** `service_price` can be aggregated by service, staff member, date, or appointment status to support business performance analysis.
- **Appointment status:** Cancelled appointments should be distinguished from completed appointments when calculating revenue and service demand.
- **Date interpretation:** The sample suggests that `date` represents the booking creation or recording date. Confirm this against the original booking system before conducting time-based analyses.