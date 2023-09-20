from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Contract(models.Model):

    seller = models.CharField(max_length=30, help_text="Enter Seller's Name")
    buyer = models.CharField(max_length=30, help_text="Enter Buyer's Name")
    listingAgent = models.CharField(max_length=30, help_text="Enter Listing Agent")
    buyingAgent = models.CharField(max_length=30, help_text="Enter Buying Agent")
    price = models.PositiveBigIntegerField(help_text="Enter Price")
    contractDate = models.DateTimeField(default=timezone.now, help_text="Enter Date of Contract")
    address1 = models.CharField(max_length=30, help_text="Enter Address1")
    address2 = models.CharField(max_length=30, null=True, help_text="Enter Address2")
    city = models.CharField(max_length=30, help_text="Enter City")
    state = models.CharField(max_length=2, help_text="Enter Two Letter State")
    zip = models.CharField(max_length=9, help_text="Enter Zip Code")
    addDate = models.DateField(auto_now_add=True, null=True, verbose_name="created at")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        ordering = ["seller"]

    def __str__(self):
        """Return a string representation of the model."""
        return self.buyer

class ContractDetail(models.Model):
    CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, null=True)
    contractPDF = models.FileField(upload_to='contracts/%Y/%m/%d',help_text="Attach Contract",blank=True, null=True)
    mortgage = models.CharField(max_length=30, default="Y", choices = CHOICES, help_text="Is there a mortgage?")
    mortgageAmount = models.PositiveBigIntegerField(default=0, help_text= "Enter Mortgage Amount")
    escrowAmount = models.PositiveBigIntegerField(help_text= "Enter Escrow Amount")
    closedContract = models.BooleanField(default=False)
    comments = models.TextField(help_text = "Enter pertinent information")
    updatedAt = models.DateField(auto_now=True, verbose_name="updated at")
    closeDate = models.DateField(null = True, help_text="Expected close date:")
    closingDocumentsPDF = models.FileField(upload_to='closingdocs/%Y/%m/%d', help_text = "Attach closing documents", blank=True, null=True)
    closedContractComments = models.TextField(default = 'No Comment', help_text="Final thoughts?")

    class Meta:
        ordering = ["comments"]
        verbose_name = "Contract Details"

    def __str__(self):
        """Return a string representation of the model."""
        return self.mortgageAmount


class Person(models.Model):
    contracts = models.ManyToManyField(Contract) #, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=30, default = None, blank=True,  null = True, help_text="First Name")
    last_name = models.CharField(max_length=30,  default = None,  blank=True, null = True, help_text="Last Name")
    title = models.CharField(max_length=30,  default = None, blank=True, null = True, help_text="Title")
    company = models.CharField(max_length=30, default = None,  blank=True,  null = True, help_text="Company")
    email = models.EmailField(max_length=254,  default = None, blank=True,  null = True, help_text="Email")
    phone = models.CharField(max_length=30, default = None,  blank=True,  null = True, help_text="Phone")
    street = models.CharField(max_length=30,  default = None, blank=True,  null = True, help_text="Street")
    city = models.CharField(max_length=30,  default = None, blank=True,  null = True, help_text="City")
    state = models.CharField(max_length=30,  default = None, blank=True,  null = True, help_text="State")
    zip = models.CharField(max_length=10,  default = None, blank=True, null = True, help_text="Zip Code")
    role = models.CharField(max_length=10, default = None,  blank=True, null = True, help_text="What is this person's role?")

    class Meta:
        ordering = ["last_name"]
        verbose_name = "Person Database"
        verbose_name_plural = "people"

    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.first_name} {self.last_name}"

class Action(models.Model):
    ROLES = [
    ("Inspection", "Inspection"),
    ("Survey", "Survey"),
    ("TitleSearch", "titleSearch"),
    ("TermiteInspection", "TermiteInspection"),
    ("TitleInsurance", "TitleInsurance"),
    ("Lawyer", "Lawyer"),
    ("MortgageLoan", "MortgageLoan"),
    ("MoldInspection", "MoldInspection"),
    ("RadonInspection", "RadonInspection"),
    ("HandyMan", "HandyMan"),
    ("Other_Action_1", "Other_Action_1"),
    ("Other_Action_2", "Other_Action_2"),
    ("Other_Action_3", "Other_Action_3")
]
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    date_add = models.DateTimeField(auto_now_add=True, verbose_name="created at")
    action = models.CharField(max_length=30, help_text= "What is the specific action to be accomplished?", choices = ROLES)
    actionPerson = models.CharField(max_length=30, help_text="Person assigned")
    actionCompany = models.CharField(max_length=30, help_text="Person's company")
    actionNextStep = models.CharField(max_length=30)
    actionFee = models.CharField(max_length=30, help_text="Fee")
    actionDueDate = models.DateField(null=True, default='', help_text="Date due")
    updatedAt = models.DateTimeField(auto_now=True, verbose_name="updated at")

    class Meta:
        verbose_name_plural = 'actions'

    def __str__(self):
        """Return a string representation of the model."""
        return self.action





