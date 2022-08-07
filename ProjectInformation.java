public class ProjectInformation {
    // Attributes - specific to the project created
    int projectNumber;
    String projectName;
    String buildingType;
    String buildingLocation;
    int ERF;
    int totalCost;
    int totalAmountPaidCurrently;
    String deadline;

    // Methods
    public ProjectInformation(int projectNumber, String projectName, String buildingType, String buildingLocation, int ERF, int totalCost, int totalAmountPaidCurrently, String deadline){
        this.projectNumber = projectNumber;
        this.projectName = projectName;
        this.buildingType = buildingType;
        this.buildingLocation = buildingLocation;
        this.ERF = ERF;
        this.totalCost = totalCost;
        this.totalAmountPaidCurrently = totalAmountPaidCurrently;
        this.deadline = deadline;
    }

    // toString to be printed in the main project page
    public String toString()
    {
        String output = "Project number:" + projectNumber;
        output += "\nProject Name:" + projectName;
        output += "\nBuilding Type:" + buildingType;
        output += "\nBuilding Location:" + buildingLocation;
        output += "\nERF number:" + ERF;
        output += "\nTotal project cost:" + totalCost;
        output += "\nThe total amount paid to date:" + totalAmountPaidCurrently;
        output += "\nProject deadline:" + deadline;

        return output;
    }

}



