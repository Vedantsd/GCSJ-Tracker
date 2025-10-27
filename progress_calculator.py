def progress(badges):
    skill_badge_list = [
        "The Basics of Google Cloud Compute",
        "Get Started with Cloud Storage",
        "Get Started with Pub/Sub",
        "Get Started with API Gateway",
        "Get Started with Looker",
        "Get Started with Dataplex",
        "Get Started with Google Workspace Tools",
        "App Building with AppSheet",
        "Develop with Apps Script and AppSheet",
        "Build a Website on Google Cloud",
        "Set Up a Google Cloud Network",
        "Store, Process, and Manage Data on Google Cloud - Console",
        "Cloud Run Functions: 3 Ways",
        "App Engine: 3 Ways",
        "Cloud Speech API: 3 Ways",
        "Monitoring in Google Cloud",
        "Analyze Speech and Language with Google APIs",
        "Prompt Design in Vertex AI",
        "Develop Gen AI Apps with Gemini and Streamlit"
    ]

    completed = 0
    arcade_game = 0
    completed_badges = []
    completed_games = []

    for badge in badges: 
        if badge in skill_badge_list:
            completed_badges.append(badge)
            completed += 1

        if "Level 3" in badge:
            arcade_game += 1
            completed_games.append(badge)
    
    percent = int(((completed + arcade_game) / 20) * 100)
    if (percent == 100) :
        progress = "Completed"
    else: 
        progress = "Pending"

    return completed, arcade_game, progress, percent, completed_badges, completed_games
