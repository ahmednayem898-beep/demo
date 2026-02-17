import random
class Doc:
    __SAVE_MESSAGES = [
    "📄✨ Your document has been successfully saved. ✅",
    "📝💾 The document was saved using your provided information. ✔️",
    "📂🔒 Your information has been securely stored. 🔐",
    "📑🚀 The document has been created and saved successfully. 🎉",
    "🗂️✅ Your document is now saved with the submitted details. 📌",
    "📋💡 The document has been stored using your input. ✔️",
    "📝🎯 Your submission has been saved successfully. ✨",
    "📁🔔 The document has been updated and saved. ✅",
    "📄🛡️ Your details have been recorded and saved securely. 🔒",
    "🗃️🎉 The document was successfully saved using your information. ✔️"
    ]
    __SAVE_ERROR_MESSAGES = [
    "⚠️📂 We could not find the required data to complete the save. ❌",
    "🚫📝 The necessary data properties for saving are missing. ⚠️",
    "❗📄 Required information is missing. Unable to save. 🔒",
    "🔍📑 We couldn’t locate the essential data needed to save. ❌",
    "🚨💾 Saving failed due to missing required data fields. ⚠️",
    "🛑📋 The required data for saving was not found. ❌",
    "⚡📁 Some mandatory fields are missing. Please check and try again. 🔁",
    "🔒🗂️ Unable to save because necessary information is incomplete. ❗",
    "🚧📄 The system could not detect the required save properties. ⚠️",
    "❌📂 Missing required data. The document cannot be saved. 🚫"
]
    __DELETE_MESSAGES = [
    "📄✅ Your document was deleted successfully!",
    "🗂️✔️ Document deleted successfully.",
    "📝✨ Your file has been removed successfully.",
    "📁🎉 Document has been successfully deleted.",
    "🗃️✅ Your document has been removed.",
    "📂⚡ Document deleted successfully from the system.",
    "📑✅ Your file was successfully removed.",
    "🛠️✔️ Document deletion completed successfully.",
    "📄🎯 Your document has been successfully deleted!",
    "🗂️🔔 Document removed successfully from the collection."
]
    __ERROR_MESSAGES = [
    "⚠️❗ Maybe the data was not provided correctly, or I couldn’t find the necessary information.",
    "🚫📄 Unable to find the required information. Please check your data.",
    "❗📝 It seems the data was incomplete or missing necessary details.",
    "🔍📂 Could not locate the required information. Check your input.",
    "⚡📑 Some necessary data is missing or improperly provided.",
    "🚨🗂️ Data might be incorrect, or essential information is missing.",
    "🛑📋 Unable to process because required information was not found.",
    "🔒📁 Could not find the necessary data. Please verify your input.",
    "⚠️🗃️ Missing or invalid data. Unable to retrieve required info.",
    "❌📄 The information provided is incomplete or not found."
]
    __NOT_FOUND_MESSAGES = [
    "🔍📄 I can’t find your document. Please provide the necessary information. ❗",
    "⚠️📂 Your document was not found. Kindly share the required details. 🔎",
    "🚫📝 Unable to locate your document. Please check and provide correct information. ❗",
    "❗📁 I couldn’t find your file. Please submit the necessary details. 🔐",
    "🔎📑 No document found. Please provide the required information. ⚠️",
    "🛑📄 Your document is missing. Kindly verify your information and try again. 🔁",
    "📂❌ Document not found. Please provide accurate details. 🔍",
    "🚨📋 I couldn’t locate your document. Please share the necessary information. ⚠️",
    "📁🔍 No matching document found. Kindly provide the correct details. ❗",
    "❌📄 Unable to find your document. Please ensure all required information is provided. 🔒"
]
    def getSaveSuccessMsg(self):
        return random.choice(self.__SAVE_MESSAGES)
    def getSaveErrorMsg(self):
        return random.choice(self.__SAVE_ERROR_MESSAGES)
    def getDeleteMsg(self):
        return random.choice(self.__DELETE_MESSAGES)
    def getDeleteErrorMsg(self):
        return random.choice(self.__ERROR_MESSAGES)
    def getFindErrorMsg(self):
        return random.choice(self.__NOT_FOUND_MESSAGES)

