thinkar_device_tool_battery = {
    "name": "thinkar_device_tool_battery",
    "description": "Get battery information from the ThinkAR glasses. The user may express their intent in different ways, such as 'what's my battery level', 'check battery status', or 'how much battery do I have left'.",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "operation": {
                "type": "STRING",
                "enum": ["get"],
                "description": "Use 'get' to check the current battery status."
            }
        },
        "required": ["operation"]
    }
}


thinkar_device_tool_brightness = {
    "name": "thinkar_device_tool_brightness",
    "description": "Control display brightness. The user may express their intent in different ways, such as 'set brightness to 50%' or 'increase brightness by 10%'. Also used to get the current brightness level.",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "operation": {
                "type": "STRING",
                "enum": ["set", "get"],
                "description": "Use 'set' to change brightness or 'get' to check the current level."
            },
            "level": {
                "type": "STRING",
                "description": "For the 'set' operation, provide a numeric value (0-100), a relative change (e.g., '+10', '-10'), or a keyword ('on', 'off', 'max', 'min', 'auto'). This parameter is not used for the 'get' operation."
            }
        },
        "required": ["operation"]
    }
}


thinkar_device_tool_dnd = {
    "name": "thinkar_device_tool_dnd",
    "description": "Control Do Not Disturb mode on the ThinkAR glasses. The user may express their intent in different ways, such as 'turn on do not disturb', 'enable DND', 'disable do not disturb', or 'check if DND is on'.",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "operation": {
                "type": "STRING",
                "enum": ["set", "get"],
                "description": "Use 'set' to change Do Not Disturb mode or 'get' to check the current mode."
            },
            "enabled": {
                "type": "BOOLEAN",
                "description": "Whether to enable (true) or disable (false) Do Not Disturb mode. This parameter is only used for the 'set' operation."
            }
        },
        "required": ["operation"]
    }
}

thinkar_device_tool_language = {
    "name": "thinkar_device_tool_language",
    "description": "Control ThinkAR glasses display language settings. The user may express their intent in different ways, such as 'change language to Spanish', 'set language to Chinese', 'what language is set', or 'switch to German'.",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "operation": {
                "type": "STRING",
                "enum": ["set", "get"],
                "description": "Use 'set' to change language or 'get' to check current language"
            },
            "language": {
                "type": "STRING",
                "enum": ["English", "Japanese", "Chinese", "Spanish", "French", "German", "Portuguese"],
                "description": "The display language to set for the glasses. This parameter is only used for the 'set' operation."
            }
        },
        "required": ["operation"]
    }
}


thinkar_device_tool_page_compass = {
    "name": "thinkar_device_tool_page_compass",
    "description": "Bring up compass page in glasses to show directional orientation. The user may express their intent in different ways, such as 'show compass', 'open compass', 'which direction am I facing', or 'show me north'.",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "operation": {
                "type": "STRING",
                "enum": ["set"],
                "description": "Show compass page"
            }
        },
        "required": ["operation"]
    }
}


thinkar_device_tool_page_navigation = {
    "name": "thinkar_device_tool_page_navigation",
    "description": "Bring up navigation page in glasses and start navigation to user specified destination. Can be triggered alone or after showing the point of interest widget. The user may express their intent in different ways, such as 'navigate to Central Park', 'get directions to the nearest gas station', or 'show me the way to 123 Main Street'.",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "operation": {
                "type": "STRING",
                "enum": ["set"],
                "description": "Set translation arguments and start navigation"
            },
            "destination": {
                "type": "STRING",
                "description": "Address or location name of the destination (maximum 100 characters)"
            },
            "mode": {
                "type": "STRING",
                "enum": ["walking", "cycling", "driving"],
                "description": "Method of travel for navigation routing"
            }
        },
        "required": ["operation", "destination", "mode"]
    }
}

thinkar_device_tool_page_take_AI_photo = {
    "name": "thinkar_device_tool_page_take_AI_photo",
    "description": "Activate the ThinkAR glasses camera to capture a single photo for AI analysis. CRITICAL: ALWAYS call this tool FIRST when users ask visual identification or analysis questions including: 'what's this?', 'what's that?', 'check this out', 'what is this?', 'what is that?', 'look at this', 'can you see this?', 'what am I holding?', 'what am I looking at?', 'identify this', 'describe the scene', 'tell me about this', 'analyze this', 'examine this', or 'take an AI photo'. Do NOT attempt to answer any visual questions without first capturing the image. After calling, WAIT for the image input—do not fabricate results. When the analysis arrives, summarize the findings in at most 2 short sentences in the user's language, suitable for on-screen display and TTS.",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "operation": {
                "type": "STRING",
                "enum": ["get"],
                "description": "Use 'get' to activate camera and take a photo for AI analysis"
            }
        },
        "required": ["operation"]
    }
}


thinkar_device_tool_page_take_photo = {
    "name": "thinkar_device_tool_page_take_photo",
    "description": "Activate the ThinkAR glasses camera to take a photo and save it locally. Use when the user requests a photo WITHOUT AI analysis (e.g., 'take a photo', 'snap a picture', 'capture an image', 'save a photo'). Do not perform analysis; after capture, confirm in ≤1 sentence.",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "operation": {
                "type": "STRING",
                "enum": ["set"],
                "description": "Use 'set' to activate camera and take a photo for local storage"
            }
        },
        "required": ["operation"]
    }
}




thinkar_device_tool_page_take_video = {
    "name": "thinkar_device_tool_page_take_video",
    "description": "Activate the ThinkAR glasses camera module to record video for a specified duration. The user may express their intent in different ways, such as 'record a video', 'start recording for 30 seconds', 'take a 1 minute video', or 'record for 3 minutes'.",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "operation": {
                "type": "STRING",
                "enum": ["set"],
                "description": "Use 'set' to start video recording"
            },
            "duration": {
                "type": "STRING",
                "enum": ["15", "30", "60", "180"],
                "description": "Duration of video recording in seconds (15s, 30s, 60s, or 180s)"
            }
        },
        "required": ["operation", "duration"]
    }
}

thinkar_device_tool_page_teleprompter = {
    "name": "thinkar_device_tool_page_teleprompter",
    "description": "Activate the ThinkAR glasses teleprompter page with specified script and settings. The user may express their intent in different ways, such as 'start teleprompter', 'load script for teleprompter', 'begin teleprompting', or 'show teleprompter with large font'.",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "operation": {
                "type": "STRING",
                "enum": ["set"],
                "description": "Use 'set' to configure and start teleprompter"
            },
            "script_name": {
                "type": "STRING",
                "description": "Name or identifier of the teleprompter script to load"
            },
            "mode": {
                "type": "STRING",
                "enum": ["manual", "cruise", "AI"],
                "description": "Scrolling mode for the teleprompter (manual control, automatic cruise, or AI-controlled)"
            },
            "font_size": {
                "type": "STRING",
                "enum": ["large", "medium", "small"],
                "description": "Font size for script display"
            }
        },
        "required": ["operation", "script_name", "mode", "font_size"]
    }
}


thinkar_device_tool_page_translation = {
    "name": "thinkar_device_tool_page_translation",
    "description": "Activate the ThinkAR glasses translation page with specified language settings. The user may express their intent in different ways, such as 'translate from English to Chinese', 'start translation mode', 'translate this to Spanish', or 'show bilingual translation'. When executed successfully, the client will move to the translation page. Complete the turn and remain silent and wait for the next user input instead of replying. By default, set bilingual to false, unless the user explicitly asks for bilingual translation.",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "operation": {
                "type": "STRING",
                "enum": ["set"],
                "description": "Use 'set' to configure and start translation mode"
            },
            "source_lang": {
                "type": "STRING",
                "enum": ["English", "Japanese", "Chinese", "French", "German", "Indonesian", "Arabic", "Thai"],
                "description": "The source language to translate from"
            },
            "target_lang": {
                "type": "STRING",
                "enum": ["English", "Japanese", "Chinese", "Spanish", "Indonesian", "Greek", "Thai"],
                "description": "The target language to translate to"
            },
            "bilingual": {
                "type": "BOOLEAN",
                "description": "Whether to show both source transcription and target translation (true) OR only target translation (false). By default, it is false."
            }
        },
        "required": ["operation", "source_lang", "target_lang", "bilingual"]
    }
}

thinkar_device_tool_screen_mode = {
    "name": "thinkar_device_tool_screen_mode",
    "description": "Control which parts of the ThinkAR glasses display are active. The user may express their intent in different ways, such as 'turn off left screen', 'enable right screen only', or 'turn on both screens' or 'turn off screens'. Also used to get the current screen mode.",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "operation": {
                "type": "STRING",
                "enum": ["set", "get"],
                "description": "Use 'set' to change screen mode or 'get' to check the current mode."
            },
            "mode": {
                "type": "STRING",
                "enum": ["left_only", "right_only", "both", "off"],
                "description": "For the 'set' operation, specify which screens should be active: 'left_only' (only left eye), 'right_only' (only right eye), 'both' (both eyes), or 'off' (neither). This parameter is not used for the 'get' operation."
            }
        },
        "required": ["operation"]
    }
}

thinkar_device_tool_version = {
    "name": "thinkar_device_tool_version",
    "description": "Get ThinkAR glasses firmware version and hardware information. The user may express their intent in different ways, such as 'what's my firmware version', 'show device info', 'check system information', 'what version am I running', or 'display hardware details'.",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "operation": {
                "type": "STRING",
                "enum": ["get"],
                "description": "Use 'get' to retrieve firmware version, MAC address, serial number, and user ID"
            }
        },
        "required": ["operation"]
    }
}



thinkar_device_tool_volume = {
    "name": "thinkar_device_tool_volume",
    "description": "Control device audio volume. The user may express their intent in different ways, such as 'set volume to 50%', 'increase volume by 10%', 'mute', or 'unmute'. Also used to get the current volume level.",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "operation": {
                "type": "STRING",
                "enum": ["set", "get"],
                "description": "Use 'set' to change volume or 'get' to check current level"
            },
            "level": {
                "type": "STRING",
                "description": "For the 'set' operation, provide a numeric value (0-100), a relative change (e.g., '+10', '-10'), or a keyword ('mute', 'unmute', 'max', 'min'). This parameter is not used for the 'get' operation."
            }
        },
        "required": ["operation"]
        }
}


thinkar_device_tool_widget_health = {
    "name": "thinkar_device_tool_widget_health",
    "description": "Display health information from Apple Health Kit in the ThinkAR glasses health widget. The user may express their intent in different ways, such as 'show me my heart rate', 'what's my step count', 'display current health', or 'check health conditions'.",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "operation": {
                "type": "STRING",
                "enum": ["set"],
                "description": "Use 'set' to display health content in the widget"
            }
        },
        "required": ["operation"]
    }
}


thinkar_device_tool_widget_news = {
    "name": "thinkar_device_tool_widget_news",
    "description": "MANDATORY: Display news headlines in the ThinkAR glasses news widget. You MUST call this tool after Google Search for ANY news-related query. Examples: 'show me the news', 'today's headlines', 'latest news', 'current events'. NEVER skip calling this tool for news queries.",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "operation": {
                "type": "STRING",
                "enum": ["set"],
                "description": "Use 'set' to display news content in the widget"
            },
            "eventdate": {
                "type": "STRING",
                "description": "Date of the news in YYYY-MM-DD format (use latest date by default)"
            },
            "headline1": {
                "type": "STRING",
                "description": "First news headline (max 100 chars, most important story)"
            },
            "headline2": {
                "type": "STRING",
                "description": "Second news headline (max 100 chars, second most important)"
            },
            "headline3": {
                "type": "STRING",
                "description": "Third news headline (max 100 chars, third most important)"
            }
        },
        "required": ["operation", "eventdate", "headline1", "headline2", "headline3"]
    }
}


thinkar_device_tool_widget_point_of_interest = {
    "name": "thinkar_device_tool_widget_point_of_interest",
    "description": "Display points of interest in the ThinkAR glasses navigation widget. The user may express their intent in different ways, such as 'show nearby restaurants', 'find points of interest', 'display navigation options', or 'show places to visit'.",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "operation": {
                "type": "STRING",
                "enum": ["set"],
                "description": "Use 'set' to display points of interest for navigation"
            },
            "poi1": {
                "type": "STRING",
                "description": "First point of interest (maximum 30 characters)"
            },
            "poi2": {
                "type": "STRING",
                "description": "Second point of interest (maximum 30 characters)"
            },
            "poi3": {
                "type": "STRING",
                "description": "Third point of interest (maximum 30 characters)"
            },
            "poi4": {
                "type": "STRING",
                "description": "Fourth point of interest (maximum 30 characters)"
            },
            "poi5": {
                "type": "STRING",
                "description": "Fifth point of interest (maximum 30 characters)"
            }
        },
        "required": ["operation", "poi1", "poi2", "poi3", "poi4", "poi5"]
    }
}



thinkar_device_tool_widget_sports = {
    "name": "thinkar_device_tool_widget_sports",
    "description": "MANDATORY: Display sports headlines and game summaries in the ThinkAR glasses sports widget. You MUST call this tool after Google Search for ANY sports-related query. Examples: 'Lakers game results', 'cricket match updates', 'NBA finals today', 'soccer scores'. NEVER skip calling this tool for sports queries.",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "operation": {
                "type": "STRING",
                "enum": ["set"],
                "description": "Use 'set' to display sports content in the widget"
            },
            "eventdate": {
                "type": "STRING",
                "description": "Date of the sports event in YYYY-MM-DD format (use latest date by default)"
            },
            "team1": {
                "type": "STRING",
                "description": "First team name (max 4 chars, e.g., 'LAL', 'BOS', 'NY')"
            },
            "score1": {
                "type": "STRING",
                "description": "First team score (max 5 chars, e.g., '108', '95-89', '131/1')"
            },
            "team2": {
                "type": "STRING",
                "description": "Second team name (max 4 chars, e.g., 'GSW', 'MIA', 'CHI')"
            },
            "score2": {
                "type": "STRING",
                "description": "Second team score (max 5 chars, e.g., '102', '87-92', '123/9')"
            }
        },
        "required": ["operation", "eventdate", "team1", "score1", "team2", "score2"]
    }
}


thinkar_device_tool_widget_weather = {
    "name": "thinkar_device_tool_widget_weather",
    "description": "MANDATORY: Display current weather information in the ThinkAR glasses weather widget. You MUST call this tool after Google Search for ANY weather-related query. Examples: 'show me the weather', 'what's the temperature', 'current weather', 'weather forecast'. NEVER skip calling this tool for weather queries.",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "operation": {
                "type": "STRING",
                "enum": ["set"],
                "description": "Use 'set' to display weather content in the widget"
            },
            "eventdate": {
                "type": "STRING",
                "description": "Date of the weather in YYYY-MM-DD format (use latest date by default)"
            },
            "location": {
                "type": "STRING",
                "description": "Location name (max 20 chars, e.g., 'New York', 'London', 'Tokyo')"
            },
            "icon": {
                "type": "STRING",
                "enum": ["sunny", "cloudy", "overcast", "rainy", "snowy", "foggy"],
                "description": "Weather icon type (choose based on current conditions)"
            },
            "status": {
                "type": "STRING",
                "description": "Weather condition (max 15 chars, e.g., 'Sunny', 'Light Rain', 'Cloudy', 'Heavy Rain')"
            },
            "temp": {
                "type": "STRING",
                "description": "Temperature (max 4 chars, e.g., '72°F', '22°C', '-5°C')"
            }
        },
        "required": ["operation", "eventdate", "location", "icon", "status", "temp"]
    }
}


thinkar_device_tool_widget_stock_ticker = {
    "name": "thinkar_device_tool_widget_stock_ticker",
    "description": "MANDATORY: Display stock information in the ThinkAR glasses stock ticker widget. You MUST call this tool after web search for ANY stock-related query. Examples: 'show me MSFT stock', 'check Apple stock price', 'display Tesla ticker', 'what's Amazon stock price'. NEVER skip calling this tool for stock queries. Use recent 15-day price data for price_line chart and provide the details in the same order and this is MANDATORY.",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "operation": {
                "type": "STRING",
                "enum": ["set"],
                "description": "Use 'set' to display stock content in the widget"
            },
            "eventdate": {
                "type": "STRING",
                "description": "Date of stock price in YYYY-MM-DD format (use most recent trading date)"
            },
            "ticker": {
                "type": "STRING",
                "maxLength": 10,
                "description": "Stock ticker symbol (max 10 chars, e.g., 'AAPL', 'MSFT', 'TSLA')"
            },
            "name": {
                "type": "STRING",
                "maxLength": 20,
                "description": "Company name (max 20 chars, e.g., 'Apple Inc', 'Microsoft Corp')"
            },
            "price_line": {
                "type": "ARRAY",
                "items": {
                    "type": "INTEGER"
                },
                "minItems": 15,
                "maxItems": 15,
                "description": "Array of exactly 15 integers representing price points for 15-day chart (15 points) rounded to the nearest whole number."
            },
            "price": {
                "type": "STRING",
                "maxLength": 15,
                "description": "Current stock price with 2 decimal places (max 15 chars, format: '150.25', '2,500.00')"
            },
            "change_pct": {
                "type": "STRING",
                "maxLength": 15,
                "description": "Percentage change with 2 decimal places and % sign (max 15 chars, format: '+2.50%', '-1.25%', '0.00%')"
            }
        },
        "required": ["operation", "eventdate", "ticker", "name", "price_line", "price", "change_pct"]
    }
}



















