import java.util.*;

public class ProjectProgram {

    public static void main(String[] args)
    {
        // Variables for information to be requested for customer + architect + contractor
        String customerName;
        String customerSurname;
        int customerNum;
        String customerEmail;
        String customerAddress;

        String architectName;
        String architectSurname;
        int architectNum;
        String architectEmail;
        String architectAddress;

        String contractorName;
        String contractorSurname;
        int contractorNum;
        String contractorEmail;
        String contractorAddress;

        // input
        Scanner input = new Scanner(System.in);

        // Customers information requested
        System.out.println("Enter customer first name: ");
        input = new Scanner(System.in);
        customerName = input.nextLine();

        System.out.println("Enter the customer second name: ");
        input = new Scanner(System.in); 
        customerSurname = input.nextLine();

        System.out.println("Enter the customer phone number: ");
        input = new Scanner(System.in); 
        customerNum = input.nextInt();

        System.out.println("Enter the customer email: ");
        input = new Scanner(System.in); 
        customerEmail = input.nextLine();

        System.out.println("Enter the customer address: ");
        input = new Scanner(System.in); 
        customerAddress = input.nextLine();
        System.out.println("\n");

        // user-defined data type - PersonInformation
        // New object called - customer - created in PersonInformation - class
        PersonInformation customer = new PersonInformation(customerName, customerSurname, customerNum, customerEmail, customerAddress);

        // Printed out Customers details and the toString method for new object - customer - created.
        System.out.println("Customers details:");
        System.out.println(customer.toString());
        System.out.println("\n");

        // Architects information requested
        System.out.println("Enter the Architect first name: ");
        input = new Scanner(System.in);
        architectName = input.nextLine();

        System.out.println("Enter the Architect second name: ");
        input = new Scanner(System.in); 
        architectSurname = input.nextLine();

        System.out.println("Enter the Architects phone number: ");
        input = new Scanner(System.in); 
        architectNum = input.nextInt();

        System.out.println("Enter the Architects email: ");
        input = new Scanner(System.in); 
        architectEmail = input.nextLine();

        System.out.println("Enter the Architects address: ");
        input = new Scanner(System.in);
        architectAddress = input.nextLine();
        System.out.println("\n");

        // user-defined data type - PersonInformation
        // New object called  - architect - created in PersonInformation - class
        PersonInformation architect = new PersonInformation(architectName, architectSurname, architectNum, architectEmail, architectAddress);

        // Printed out Architects details and the toString method for new object - architect - created.
        System.out.println("Architects details:");
        System.out.println(architect.toString());
        System.out.println("\n");

        // Contractors information requested
        System.out.println("Please enter the Contractors first name: ");
        input = new Scanner(System.in); 
        contractorName = input.nextLine();

        System.out.println("Enter the Contractors second name: ");
        input = new Scanner(System.in); 
        contractorSurname = input.nextLine();

        System.out.println("Enter the Contractors phone number: ");
        input = new Scanner(System.in); 
        contractorNum = input.nextInt();

        System.out.println("Enter the Contractors email: ");
        input = new Scanner(System.in); 
        contractorEmail = input.nextLine();

        System.out.println("Enter the Contractors address: ");
        input = new Scanner(System.in); 
        contractorAddress = input.nextLine();
        System.out.println("\n");

        // user-defined data type - PersonInformation
        // New object called - contractor - created in PersonInformation - class
        PersonInformation contractor = new PersonInformation(contractorName, contractorSurname, contractorNum, contractorEmail, contractorAddress);

        // Printed out Contractors details and the toString method for new object - Contractor - created.
        System.out.println("Contractor details:");
        System.out.println(contractor.toString());
        System.out.println("\n");



        //==================| Project Details |===================\\

        // Variables for information to be requested for project to be created
        int projectNumber = 0;
        String buildingType = null;
        String projectName = null;
        String buildingLocation = null;
        int ERF = 0;
        int totalCost = 0;
        int totalAmountPaidCurrently = 0;
        String deadline = null;

        //----------------- Project information requested
        System.out.println("Enter the project number: ");
        input = new Scanner(System.in); 
        projectNumber = input.nextInt();

        System.out.println("Enter the building type: ");
        input = new Scanner(System.in); 
        buildingType = input.nextLine();

        System.out.println("Enter the project name (leave blank for auto generate): ");
        input = new Scanner(System.in); 
        projectName = input.nextLine();

        // If statement to auto generate of a project name
        if (projectName.equals(""))
        {
            projectName = buildingType + " " + customerSurname; // project name auto generated if user selects to leave the project name blank
        }

        System.out.println("Enter the building location: ");
        input = new Scanner(System.in); 
        buildingLocation = input.nextLine();

        System.out.println("Enter the ERF number: ");
        input = new Scanner(System.in); 
        ERF = input.nextInt();

        System.out.println("Enter the total cost of project: ");
        input = new Scanner(System.in); 
        totalCost = input.nextInt();

        System.out.println("Enter the total amount paid to date: ");
        input = new Scanner(System.in); 
        totalAmountPaidCurrently = input.nextInt();

        System.out.println("Enter the project deadline in this format dd/mm/yyyy: ");
        input = new Scanner(System.in); 
        deadline = input.nextLine();
        System.out.println("\n");

        // user-defined data type - projectDetails
        // New object called - newProject - created in projectDetails - class
        ProjectInformation newProject = new ProjectInformation(projectNumber, projectName, buildingType, buildingLocation, ERF, totalCost, totalAmountPaidCurrently, deadline);

        // Printed out Project details and the toString method on new object - Project - created
        System.out.println(newProject.toString());
        System.out.println("\n");



        //-----------| Print menu |--------------
        while (true)
        {
            String menuSelection;
            input = new Scanner(System.in); // user input requested based on menu options listed below


            System.out.println("Menu:");
            System.out.println("1 - Change due date of project");
            System.out.println("2 - Change total amount of the fee paid to date");
            System.out.println("3 - Update the contractors contact details");
            System.out.println("4 - Quit");

            menuSelection = input.nextLine();  // String menuSelection is equal to users input

            // If user selects '1' - from the menu, they will be able to update the project deadline
            if (menuSelection.equals("1"))
            {
                System.out.println("Enter the new project deadline in this format dd/mm/yyyy: ");
                input = new Scanner(System.in); 
                deadline = input.nextLine();
                System.out.println("\n");

               //New object called - projectUpdated - created - in projectDetails class
                ProjectInformation projectUpdated = new ProjectInformation(projectNumber, projectName, buildingType, buildingLocation, ERF, totalCost, totalAmountPaidCurrently, deadline);

                // Printed out toString method for new object - projectUpdated - created with the updated project deadline
                System.out.println(projectUpdated.toString());
                System.out.println("\n");
            }

            // If user selects '2' - from the menu, they will be able to update the total amount paid to date
            if (menuSelection.equals("2"))
            {
                System.out.println("Enter the total amount paid to date: ");
                input = new Scanner(System.in); 
                totalAmountPaidCurrently = input.nextInt();
                System.out.println("\n");

                // New object called - projectUpdated - created - in projectDetails class
                ProjectInformation projectUpdated = new ProjectInformation(projectNumber, projectName, buildingType, buildingLocation, ERF, totalCost, totalAmountPaidCurrently, deadline);

                // Printed out toString method for new object - projectUpdated - created with the updated total amount paid to date
                System.out.println(projectUpdated.toString());
                System.out.println("\n");

            }

            // If user selects '3' - from the menu, they will be able to update the contractors details
            if (menuSelection.equals("3"))
            {
                System.out.println("Update the contractors details: ");
                input = new Scanner(System.in);

                System.out.println("Enter the Contractors first name: ");
                input = new Scanner(System.in); 
                contractorName = input.nextLine();

                System.out.println("Enter the Contractors second name: ");
                input = new Scanner(System.in); 
                contractorSurname = input.nextLine();

                System.out.println("Enter the Contractors phone number: ");
                input = new Scanner(System.in); 
                contractorNum = input.nextInt();

                System.out.println("Please enter the Contractors email");
                input = new Scanner(System.in); 
                contractorEmail = input.nextLine();

                System.out.println("Please enter the Contractors address");
                input = new Scanner(System.in); 
                contractorAddress = input.nextLine();
                System.out.println("\n");

                // New object called - contractorUpdated - created - in PersonInformation class
                PersonInformation contractorUpdated = new PersonInformation(contractorName, contractorSurname, contractorNum, contractorEmail, contractorAddress);

                // Printed out toString method for new object - contractorUpdated - created with the updated contractors details added
                System.out.println("Updated contractor  details:");
                System.out.println(contractorUpdated.toString());
                System.out.println("\n");

            }
            // If user selects '4' - from the menu, they will exit program
            if (menuSelection.equals("4"))
            {
                System.out.println("Goodbye! ");
                break;
            }

            }
    }
}
