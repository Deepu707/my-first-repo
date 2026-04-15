# File: theatre_booking_system.py

# Theatre capacity
capacity = 350
remaining_seats = capacity

# Tracking stats
total_bookings = 0
tickets_sold = 0
rejected_bookings = 0

while remaining_seats > 0:
    # Ask for number of tickets
    tickets = int(input("Enter number of tickets (0 to exit): "))

    # Stop condition
    if tickets == 0:
        break

    # Validate ticket count
    if tickets < 1 or tickets > 15:
        print("BOOKING REJECTED - Invalid ticket count (1-15 only)")
        rejected_bookings += 1
        continue

    # Check if enough seats are available
    if tickets > remaining_seats:
        print("BOOKING REJECTED - Not enough seats available")
        rejected_bookings += 1
        continue

    # Age validation
    valid_booking = True
    for i in range(tickets):
        age = int(input(f"Enter age for person {i+1}: "))
        if age < 12:
            valid_booking = False
            break

    if valid_booking:
        print(f"BOOKING CONFIRMED - {tickets} tickets")
        total_bookings += 1
        tickets_sold += tickets
        remaining_seats -= tickets
    else:
        print("BOOKING REJECTED - Age restriction")
        rejected_bookings += 1

    # Stop if theatre is full
    if remaining_seats == 0:
        print("Theatre is now FULL. No more bookings allowed.")
        break

# Final Report
print("\n--- FINAL REPORT ---")
print("Total Bookings:", total_bookings)
print("Total Tickets Sold:", tickets_sold)
print("Rejected Bookings:", rejected_bookings)
print("Remaining Seats:", remaining_seats)
