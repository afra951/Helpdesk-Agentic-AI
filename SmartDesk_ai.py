# ============================================================
# SMARTDESK AI
# Agentic AI-Powered IT Helpdesk Assistant
# ============================================================

import json
from datetime import datetime
from collections import Counter


# ============================================================
# 1. IT KNOWLEDGE BASE
# ============================================================

knowledge_base = {

    "Network": {
        "keywords": [
            "wifi", "wi-fi", "internet", "network",
            "slow internet", "connection", "vpn",
            "connected but no internet"
        ],

        "solutions": [
            "Check whether Wi-Fi is turned on.",
            "Restart your Wi-Fi router.",
            "Forget the Wi-Fi network and reconnect.",
            "Restart your computer.",
            "Run the network troubleshooter."
        ]
    },


    "System": {
        "keywords": [
            "slow", "hang", "hanging",
            "not starting", "boot", "restart",
            "overheating", "storage",
            "blue screen", "battery"
        ],

        "solutions": [
            "Restart your computer.",
            "Close unnecessary applications.",
            "Check available storage space.",
            "Check Task Manager for high CPU or memory usage.",
            "Run a system update."
        ]
    },


    "Printer": {
        "keywords": [
            "printer", "printing",
            "print", "scanner", "offline",
            "paper", "spooler"
        ],

        "solutions": [
            "Check whether the printer is turned on.",
            "Check the printer cable or Wi-Fi connection.",
            "Restart the printer.",
            "Set the printer as the default printer.",
            "Restart the print spooler."
        ]
    },


    "Account": {
        "keywords": [
            "password", "login",
            "account", "locked",
            "access", "permission",
            "authentication", "sign in"
        ],

        "solutions": [
            "Check your username and password.",
            "Try resetting your password.",
            "Check whether your account is locked.",
            "Clear browser cache and try again.",
            "Contact the administrator for access permissions."
        ]
    },


    "Email": {
        "keywords": [
            "email", "mail",
            "inbox", "send",
            "receive", "attachment",
            "outlook"
        ],

        "solutions": [
            "Check your internet connection.",
            "Verify the recipient's email address.",
            "Check whether your inbox storage is full.",
            "Restart your email application.",
            "Try sending or receiving the email again."
        ]
    },


    "Software": {
        "keywords": [
            "software", "application",
            "app", "install",
            "crash", "error",
            "not opening", "update",
            "installation"
        ],

        "solutions": [
            "Restart the application.",
            "Check for software updates.",
            "Restart your computer.",
            "Reinstall the application.",
            "Check the error message for more details."
        ]
    },


    "Security": {
        "keywords": [
            "phishing", "suspicious",
            "malware", "virus",
            "unknown login",
            "security", "hacked"
        ],

        "solutions": [
            "Do not click suspicious links or attachments.",
            "Do not share your password.",
            "Verify the sender or source.",
            "Change your password if you suspect account compromise.",
            "Report the suspicious activity to IT security."
        ]
    },


    "File_Storage": {
        "keywords": [
            "file", "folder",
            "storage full",
            "deleted file",
            "cloud", "drive",
            "shared folder",
            "sync"
        ],

        "solutions": [
            "Check available storage space.",
            "Check whether you have permission to access the file.",
            "Check the recycle bin for deleted files.",
            "Check your cloud synchronization status.",
            "Contact IT if the file cannot be recovered."
        ]
    }
}


# ============================================================
# 2. MEMORY AND DATA STORAGE
# ============================================================

conversation_memory = []

tickets = []

feedback_data = []


# ============================================================
# 3. ISSUE CLASSIFICATION AGENT
# ============================================================

def classify_issue(user_issue):

    user_issue = user_issue.lower()

    category_scores = {}

    for category, data in knowledge_base.items():

        score = 0

        for keyword in data["keywords"]:

            if keyword in user_issue:

                score += 1

        category_scores[category] = score

    best_category = max(
        category_scores,
        key=category_scores.get
    )

    if category_scores[best_category] == 0:

        return "Unknown"

    return best_category


# ============================================================
# 4. PRIORITY DETECTION
# ============================================================

def detect_priority(user_issue):

    issue = user_issue.lower()

    critical_keywords = [
        "entire office",
        "server down",
        "all systems",
        "network down",
        "data loss",
        "security breach",
        "company down"
    ]

    high_keywords = [
        "urgent",
        "cannot work",
        "can't work",
        "not starting",
        "crash",
        "locked",
        "hacked"
    ]

    low_keywords = [
        "how to",
        "information",
        "change settings",
        "request"
    ]

    for keyword in critical_keywords:

        if keyword in issue:

            return "Critical"

    for keyword in high_keywords:

        if keyword in issue:

            return "High"

    for keyword in low_keywords:

        if keyword in issue:

            return "Low"

    return "Medium"


# ============================================================
# 5. CONFIDENCE DETECTION
# ============================================================

def calculate_confidence(user_issue, category):

    issue = user_issue.lower()

    if category == "Unknown":

        return 30

    matched_keywords = 0

    for keyword in knowledge_base[category]["keywords"]:

        if keyword in issue:

            matched_keywords += 1

    confidence = min(
        50 + matched_keywords * 20,
        100
    )

    return confidence


# ============================================================
# 6. KNOWLEDGE RETRIEVAL (RAG-STYLE)
# ============================================================

def retrieve_solution(category):

    if category == "Unknown":

        return [
            "I could not identify the exact issue.",
            "Please provide more details.",
            "You may create a support ticket for IT assistance."
        ]

    return knowledge_base[category]["solutions"]


# ============================================================
# 7. CONVERSATION MEMORY
# ============================================================

def save_memory(user_issue, category, priority):

    memory = {

        "issue": user_issue,

        "category": category,

        "priority": priority,

        "time": str(datetime.now())

    }

    conversation_memory.append(memory)


# ============================================================
# 8. CREATE SUPPORT TICKET TOOL
# ============================================================

def create_ticket(issue, category, priority):

    ticket_id = "IT-" + str(len(tickets) + 1).zfill(4)

    ticket = {

        "ticket_id": ticket_id,

        "issue": issue,

        "category": category,

        "priority": priority,

        "status": "Open",

        "created_at": str(datetime.now())

    }

    tickets.append(ticket)

    return ticket


# ============================================================
# 9. CHECK TICKET STATUS TOOL
# ============================================================

def check_ticket(ticket_id):

    for ticket in tickets:

        if ticket["ticket_id"].lower() == ticket_id.lower():

            return ticket

    return None


# ============================================================
# 10. FEEDBACK SYSTEM
# ============================================================

def collect_feedback(issue, solved):

    feedback = {

        "issue": issue,

        "solved": solved,

        "time": str(datetime.now())

    }

    feedback_data.append(feedback)


# ============================================================
# 11. SENTIMENT DETECTION
# ============================================================

def detect_sentiment(user_issue):

    issue = user_issue.lower()

    frustrated_words = [
        "frustrated",
        "angry",
        "nothing working",
        "annoyed",
        "urgent",
        "help me",
        "worst"
    ]

    for word in frustrated_words:

        if word in issue:

            return "Frustrated"

    return "Neutral"


# ============================================================
# 12. ISSUE ANALYSIS AGENT
# ============================================================

def analyze_issue(user_issue):

    category = classify_issue(user_issue)

    priority = detect_priority(user_issue)

    confidence = calculate_confidence(
        user_issue,
        category
    )

    sentiment = detect_sentiment(
        user_issue
    )

    save_memory(
        user_issue,
        category,
        priority
    )

    return {

        "category": category,

        "priority": priority,

        "confidence": confidence,

        "sentiment": sentiment
    }


# ============================================================
# 13. INTERACTIVE TROUBLESHOOTING AGENT
# ============================================================

def interactive_troubleshooting(issue, solutions):

    print("\n🔧 STARTING TROUBLESHOOTING")

    print("-" * 40)

    for i, solution in enumerate(solutions, start=1):

        print(f"\nStep {i}: {solution}")

        response = input(
            "\nDid this solve your problem? (yes/no): "
        ).lower().strip()

        if response in ["yes", "y"]:

            print(
                "\n🎉 Great! Your problem has been resolved."
            )

            collect_feedback(
                issue,
                True
            )

            return True

    print(
        "\n⚠️ The problem could not be resolved automatically."
    )

    collect_feedback(
        issue,
        False
    )

    return False


# ============================================================
# 14. HELP DESK ANALYTICS
# ============================================================

def show_analytics():

    print("\n")

    print("=" * 45)

    print("📊 SMARTDESK AI ANALYTICS")

    print("=" * 45)

    print(
        "\nTotal Issues:",
        len(conversation_memory)
    )

    print(
        "Tickets Created:",
        len(tickets)
    )

    solved_count = sum(

        1 for feedback in feedback_data

        if feedback["solved"]

    )

    unresolved_count = len(feedback_data) - solved_count

    print(
        "Issues Solved:",
        solved_count
    )

    print(
        "Issues Unresolved:",
        unresolved_count
    )

    if feedback_data:

        resolution_rate = (

            solved_count / len(feedback_data)

        ) * 100

        print(
            "Resolution Rate:",
            round(resolution_rate, 2),
            "%"
        )

    if conversation_memory:

        categories = [

            item["category"]

            for item in conversation_memory

        ]

        most_common = Counter(
            categories
        ).most_common(1)

        print(
            "Most Common Category:",
            most_common[0][0]
        )


# ============================================================
# 15. DISPLAY TICKET
# ============================================================

def display_ticket(ticket):

    print("\n")

    print("=" * 40)

    print("🎫 SUPPORT TICKET")

    print("=" * 40)

    for key, value in ticket.items():

        print(
            f"{key.replace('_', ' ').title()}: {value}"
        )


# ============================================================
# 16. MAIN SMARTDESK AI AGENT
# ============================================================

def smartdesk_agent():

    print("\n")

    print("=" * 55)

    print("🤖 WELCOME TO SMARTDESK AI")

    print("Agentic AI-Powered IT Helpdesk Assistant")

    print("=" * 55)


    while True:

        print("\n")

        print("1. Report an IT Issue")

        print("2. Check Ticket Status")

        print("3. View Analytics")

        print("4. View Conversation Memory")

        print("5. Exit")


        choice = input(
            "\nChoose an option (1-5): "
        ).strip()


        # ====================================================
        # OPTION 1 - REPORT ISSUE
        # ====================================================

        if choice == "1":

            issue = input(
                "\nDescribe your IT problem:\n"
            )


            analysis = analyze_issue(issue)


            category = analysis["category"]

            priority = analysis["priority"]

            confidence = analysis["confidence"]

            sentiment = analysis["sentiment"]


            print("\n")

            print("=" * 40)

            print("🧠 AI ISSUE ANALYSIS")

            print("=" * 40)


            print(
                "Issue:",
                issue
            )

            print(
                "Category:",
                category
            )

            print(
                "Priority:",
                priority
            )

            print(
                "AI Confidence:",
                str(confidence) + "%"
            )

            print(
                "User Sentiment:",
                sentiment
            )


            if sentiment == "Frustrated":

                print(
                    "\n💬 I understand this situation may be frustrating."
                )

                print(
                    "Let's solve this step-by-step."
                )


            # ================================================
            # SMART ESCALATION
            # ================================================

            if priority == "Critical":

                print(
                    "\n🚨 CRITICAL ISSUE DETECTED!"
                )

                print(
                    "Escalating directly to IT support."
                )


                ticket = create_ticket(
                    issue,
                    category,
                    priority
                )


                display_ticket(ticket)


                continue


            # ================================================
            # LOW CONFIDENCE
            # ================================================

            if confidence < 50:

                print(
                    "\n⚠️ I am not confident enough to diagnose this issue."
                )

                print(
                    "I recommend creating a support ticket."
                )


                response = input(
                    "\nCreate ticket? (yes/no): "
                ).lower().strip()


                if response in ["yes", "y"]:

                    ticket = create_ticket(
                        issue,
                        category,
                        priority
                    )


                    display_ticket(ticket)


                continue


            # ================================================
            # RETRIEVE KNOWLEDGE
            # ================================================

            solutions = retrieve_solution(
                category
            )


            print("\n📚 Knowledge Retrieved")

            print(
                f"Category: {category}"
            )


            solved = interactive_troubleshooting(

                issue,

                solutions

            )


            # ================================================
            # AUTOMATIC ESCALATION
            # ================================================

            if not solved:

                print(
                    "\n🎫 Escalating issue to IT Support..."
                )


                ticket = create_ticket(

                    issue,

                    category,

                    priority

                )


                display_ticket(ticket)


        # ====================================================
        # OPTION 2 - CHECK TICKET
        # ====================================================

        elif choice == "2":

            ticket_id = input(
                "\nEnter Ticket ID: "
            )


            ticket = check_ticket(
                ticket_id
            )


            if ticket:

                display_ticket(ticket)

            else:

                print(
                    "\n❌ Ticket not found."
                )


        # ====================================================
        # OPTION 3 - ANALYTICS
        # ====================================================

        elif choice == "3":

            show_analytics()


        # ====================================================
        # OPTION 4 - MEMORY
        # ====================================================

        elif choice == "4":

            print("\n🧠 CONVERSATION MEMORY")

            print("=" * 40)


            if not conversation_memory:

                print(
                    "No previous issues found."
                )

            else:

                for i, memory in enumerate(
                    conversation_memory,
                    start=1
                ):

                    print(
                        f"\n{i}. Issue: {memory['issue']}"
                    )

                    print(
                        f"   Category: {memory['category']}"
                    )

                    print(
                        f"   Priority: {memory['priority']}"
                    )


        # ====================================================
        # OPTION 5 - EXIT
        # ====================================================

        elif choice == "5":

            print(
                "\n👋 Thank you for using SmartDesk AI!"
            )

            print(
                "Have a great day!"
            )

            break


        # ====================================================
        # INVALID OPTION
        # ====================================================

        else:

            print(
                "\n❌ Invalid option. Please try again."
            )


# ============================================================
# START SMARTDESK AI
# ============================================================

smartdesk_agent()
