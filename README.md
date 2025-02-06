Discord Bot to Manage Channels, Roles, and Members

This is a simple Discord bot built using Python and the discord.py library. The bot can be used to manage Discord servers by:

    Deleting all existing channels in a server.
    Creating a specific number of new text channels.
    Creating roles with specific names.
    Banning all members from the server.

Features

    Delete All Channels: The bot can delete all existing channels in the server after asking for confirmation.
    Create New Channels: After deleting the channels, the bot can create a specific number of new text channels.
    Create New Roles: The bot can create multiple roles with custom names and assign them in the server.
    Ban All Members: The bot can ban all members from the server after confirmation.

Prerequisites

Before using this bot, you need to ensure that you have:

    A Discord bot token: You can create a bot on the Discord Developer Portal.
    The bot needs the following permissions:
        Manage Channels: For creating and deleting channels.
        Manage Roles: For creating roles.
        Ban Members: For banning members.

You can assign these permissions in the Discord Developer Portal when you generate the invite link for your bot.
Setup

    Install the required Python dependencies:

pip install discord.py

Replace the following variables in the script with your specific information:

    TOKEN: Your bot's token.
    GUILD_ID: The ID of the server (guild) you want to manage.
    CHANNEL_NAME: The name for the new channels created by the bot.
    CHANNEL_COUNT: The number of new channels you want to create.
    ROLE_NAME: The base name for the roles created by the bot.
    ROLE_COUNT: The number of roles you want to create.

Run the script with the following command:

    python bot.py

Bot Actions

    Delete All Channels: The bot will ask for confirmation before deleting all the channels in the specified guild.
    Create New Channels: The bot will then create a specified number of new text channels with the name specified in CHANNEL_NAME.
    Create New Roles: After creating the channels, the bot will ask for confirmation to create the roles. It will create the roles with names like Role name 1, Role name 2, etc.
    Ban All Members: Finally, after confirming, the bot will proceed to ban all members from the server.

Example Flow

When the bot is running, it will prompt the following in the console:

    Are you sure you want to delete all channels in [guild name]? (y/n)
    Are you sure you want to create [ROLE_COUNT] roles in [guild name]? (y/n)
    Are you sure you want to ban all members in [guild name]? (y/n)

You need to type "y" for "Yes" to proceed with each action. If you type anything other than "y", the corresponding action will be canceled.
Security Notice

    Be cautious: Deleting channels and banning members are irreversible actions. Ensure that you only use this bot on servers where you have the proper permissions and where you can safely perform these actions.
    Never share your bot token publicly: Keep the bot token safe and avoid sharing it publicly, as it allows full control of your bot.

Example Usage:

    Start the bot.
    Confirm the actions for deleting channels, creating new channels, creating roles, and banning members when prompted.
    The bot will perform the actions and close itself automatically after completing all tasks.
