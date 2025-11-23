# Healthcare Industry  :-

class Database:
    def __init__(self):
        self.data = {}
        self.data['time_slots'] = [
            "10:00 AM", "11:00 AM", "12:00 PM", "02:00 PM", "03:00 PM"
        ]

class Details(Database):
    def form_details(self):
        print("------- appointment form -------")
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        mobile_no = input("Enter your mobile number: ")
        preferred_doctor = input("Enter preferred doctor: ")

        self.data['name'] = name
        self.data['age'] = age
        self.data['mobile_no'] = mobile_no
        self.data['preferred_doctor'] = preferred_doctor

    
        print("Available Time Slots:")
        for i, slot in enumerate(self.data['time_slots'], 1):
            print(f"{i}. {slot}")

        slot_choice = int(input("Choose time slot number: ")) - 1
        if 0 <= slot_choice < len(self.data['time_slots']):
            self.data['booked_slot'] = self.data['time_slots'].pop(slot_choice)
            print("Slot booked successfully!")
        else:
            print("Invalid slot!")

class Appointment(Details):
    def appoint_status(self):
        mobile_no = input("Enter your mobile number: ")
        
        if self.data.get('mobile_no') == mobile_no:
            print("\n------ Appointment Status ------")
            print("Name:", self.data.get('name'))
            print("Age:", self.data.get('age'))
            print("Mobile No:", self.data.get('mobile_no'))
            print("Preferred Doctor:", self.data.get('preferred_doctor'))
            print("Time Slot:", self.data.get('booked_slot'))
        else:
            print("Mobile number not found!")

    def cancel_appointment(self):
        mobile_no = input("Enter your mobile number to cancel: ")

        if self.data.get('mobile_no') == mobile_no:
            # return slot back
            self.data['time_slots'].append(self.data['booked_slot'])
            self.data['booked_slot'] = None
            print("Appointment cancelled successfully!")
        else:
            print("Mobile number not found!")


obj = Appointment()

while True:
    print("\n1. Book Appointment")
    print("2. Check Appointment Status")
    print("3. Cancel Appointment")
    print("4. Exit")
    
    ch = int(input("Enter your choice: "))

    if ch == 1:
        obj.form_details()
    elif ch == 2:
        obj.appoint_status()
    elif ch == 3:
        obj.cancel_appointment()
    elif ch == 4:
        print("Exited successfully.")
        break
    else:
        print("Invalid choice!")


#  -------------------------------------------------------------------------------------------------

# School Management System :-

class stu_data():
     students={}
     stu_id=1

    
    
class new_addmission(stu_data):
    def new_add(self):
        
        student_id=stu_data.stu_id
        stu_data.stu_id=stu_data.stu_id+1

        print("-------addmission form --------")
        name=input("enter student's name :")
        age=int(input("enter student's age :"))
        classs=int(input("enter class (1-12)  :"))
        guardian_mobile=input("enter guardian mobile no.  :")
        
        if 5<=age<=18 and 1<=classs<=12 and len(guardian_mobile)==10 :
            stu_data.students[student_id]={
             "name":name,
             "age":age,
             "class":classs,
             "guardian no.":guardian_mobile
            }
            print("---admission sucessful !!!---")
            print("yoour student id is :",student_id)
        else:
            print("invalid details !!")     
class student_detail(new_addmission):
    def detail(self):
        student_id=int(input("enter your student id :"))
        if student_id in stu_data.students:
            print("------student detail------")
            
            print("name         :",stu_data.students[student_id]["name"])
            print("age          :",stu_data.students[student_id]["age"])
            print("class        :",stu_data.students[student_id]["class"])
            print("guardian no. :",stu_data.students[student_id]["guardian no."])
        else :
            print(" !!!! student does nott exist !!!!")
class update_details(student_detail):
    def update(self):
        print("--press 1 to update class---")
        print("--press 2 to update guardian no.--- ")
        choice=int(input("enter your choice :"))
        if choice==1:
            student_id=int(input("enter your student id :"))
            if student_id in self.students:
                new_class=int(input("enter your class :"))
                stu_data.students[student_id]["class"]=new_class
                print("your class is updated !!!")
            else:
                print("invalid details !!!")
        elif choice==2 :
            student_id=int(input("enter your student id :"))
            if student_id in stu_data.students:
                new_guardian_no=input("enter your guardian no. :")
                stu_data.students[student_id]["guardian no."]=new_guardian_no
                print("your guardian no. is updated !!!")
            else:
                print("invalid details !!!")
        else:
            print("invalid choice")
class remove_details(update_details):
    def delete(self):
        student_id=int(input("enter your student id :"))
        if student_id in stu_data.students:
            del stu_data.students[student_id]
            print("student's details removed successfully !!!")
        else :
            print("invalid details !!!")

        
obj=remove_details()

while True:
    print("-- press 1 to new admission  --- ")
    print("-- press 2 to view deatils   --- ")
    print("-- press 3 to update details --- ") 
    print("-- press 4 to remove details --- ")
    print("-- press 5 to exit           --- ")
    choice = int(input("enter your choice :"))

    if choice==1:
        
    
        obj.new_add()
    elif choice ==2 :
        obj.detail()
    elif choice==3:
        obj.update()
    elif choice==4:
        obj.delete()
    elif choice==5:
        print("thank you !!!")
        break
    else:
        print("invalid chioce !!!")

# --------------------------------------------------------------------------------------------

# Transport Reservation System (Bus Ticketing)  :-

class details():
    passenger = {}
    ticket_no = 1

   
    routes = {
        "Mumbai to Pune": 500,
        "Delhi to Jaipur": 600,
        "Ahmedabad to Pulasar": 1200
    }

   
    route_list = list(routes.keys())

   
    booked_seats = {route: [] for route in routes}


class passenger_data(details):

    
    def show_routes(self):
        print("--- Available Routes ---")
        for i, r in enumerate(details.route_list, start=1):
            print(f"{i}. {r} - ₹{details.routes[r]}")

    
    def passenger_detail(self):
        ticket_no = details.ticket_no
        details.ticket_no += 1

        name = input("enter your name : ")
        age = int(input("enter your age : "))
        mobile = input("enter your mobile no : ")

        print("Choose Route:")
        self.show_routes()

        
        route_no = int(input("Enter route number (1/2/3): "))

        
        if route_no < 1 or route_no > len(details.route_list):
            print("Invalid route number!")
            return

        
        route = details.route_list[route_no - 1]

        
        if len(details.booked_seats[route]) >= 40:
            print("Sorry! All seats are booked for this route.")
            return

        
        if len(mobile) != 10:
            print("Invalid mobile number!")
            return

        
        seat_no = len(details.booked_seats[route]) + 1
        details.booked_seats[route].append(seat_no)

        
        details.passenger[ticket_no] = {
            "name": name,
            "age": age,
            "mobile": mobile,
            "route": route,
            "seat_no": seat_no,
            "price": details.routes[route]
        }

        print("--- Ticket Booked Successfully! ---")
        print("Your Ticket No :", ticket_no)
        print("Seat No        :", seat_no)
        print("Route          :", route)
        print("Price          : ₹", details.routes[route])


class view(passenger_data):
    def ticket_view(self):
        ticket_no = int(input("enter your ticket no. : "))
        if ticket_no in details.passenger:
            t = details.passenger[ticket_no]
            print("---- Ticket Details ----")
            print("Name     :", t["name"])
            print("Age      :", t["age"])
            print("Mobile   :", t["mobile"])
            print("Route    :", t["route"])
            print("Seat No  :", t["seat_no"])
            print("Price    : ₹", t["price"])
        else:
            print("Invalid ticket number!")


class cancel(view):
    def cancel_ticket(self):
        ticket_no = int(input("enter your ticket no. : "))
        if ticket_no in details.passenger:
            info = details.passenger[ticket_no]
            route = info["route"]
            seat_no = info["seat_no"]


            details.booked_seats[route].remove(seat_no)

            del details.passenger[ticket_no]
            print("Your ticket cancelled successfully !!!")
        else:
            print("Invalid ticket no !!!!")



obj = cancel()

while True:
    print("===== BUS RESERVATION SYSTEM =====")
    print("press 1 to book a ticket ")
    print("press 2 to check ticket ")
    print("press 3 to cancel ticket ")
    print("press 4 to exit ")

    choice = int(input("enter your choice : "))

    if choice == 1:
        obj.passenger_detail()
    elif choice == 2:
        obj.ticket_view()
    elif choice == 3:
        obj.cancel_ticket()
    elif choice == 4:
        print("Thank You !!!")
        break
    else:
        print("Invalid choice !!!")
