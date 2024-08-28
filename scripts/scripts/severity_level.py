import sys

def get_severity_level(severity):
    severity_dict = {
        'low': 0,
        'medium': 1,
        'high': 2,
        'critical': 3
    }

    try:
        severity_word = severity.lower()

        if severity_word not in severity_dict:
            return 'high'

        severity_code = severity_dict[severity_word]

        if severity_code > 2:
            print("The scanned severity cannot be greater than high.")
            return 'high'
        
        return severity_word
    
    except Exception as e:
        return 'high'

if __name__ == "__main__":
    severity = sys.argv[1] if len(sys.argv) > 1 else "high"
    severity_result = get_severity_level(severity)
    print(f"SEVERITY_RESULT: {severity_result}")