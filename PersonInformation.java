public class PersonInformation {

    // Attributes - specific to the relevant parties included in the project (Customer, Architect, Contractor)
    String name;
    String surname;
    int mobileNumber;
    String emailAddress;
    String physicalAddress;

    // Methods
    public PersonInformation(String name, String surname, int mobileNumber, String emailAddress, String physicalAddress) // object constructor
    {
        this.name = name;
        this.surname = surname;
        this.mobileNumber = mobileNumber;
        this.emailAddress = emailAddress;
        this.physicalAddress = physicalAddress;
    }

    // toString to be printed in the main project page
    public String toString()
    {
        String output = "Name:" + name;
        output += "\nSurname:" + surname;
        output += "\nMobile Number:" + mobileNumber;
        output += "\nEmail address:" + emailAddress;
        output += "\nPhysical Address:" + physicalAddress;

        return output;

    }
}
