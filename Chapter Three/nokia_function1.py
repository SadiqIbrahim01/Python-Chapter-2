# nokia_function1
print ('List of Menu Functions\n1. Phone book\n2. Messages\n3. Chat\n4. Call register\n5. Tones\n6. Settings\n7. Call divert\n8. Games\n9. Calculator\n10. Reminder\n11. Clock\n12. Profiles\n13. SIM services')
menu_options = int (input('Welcome...Please enter an option to continue: '))

match menu_options:
    case '1':
        print ('1. Search\n2. Service Nos.\n3. Add name\n4. Erase\n5. Edit\6. Assign tone\n7. Send bcard\n8. Options\n9. Speed dials\n10. Voice')

    case '2':
        print ('1. Write messages\n2. Inbox\n3. Outbox\n4. Picture messages\n5. Templates\n6. Smileys\n7. Message settings\n8. Info service\n9. Voice mailbox number\n10. Service command editor')

    case '3':
        print ('You chose chat')

    case '4':
        print ('1. Missed calls\n2. Received calls\n3. Dialled numbers\n4. Erase recent call list\n5. Show call duration\n6. Show call costs\n7. Call cost settings\n8. Prepaid credit')

    case '5':
        print ('1. Ringing tone\n2. Ringing volume\n3. Incoming call alert\n4. Composer\n5. Message alert tone\n6. Keypad tones\n7. Warning and game tones\n8. Vibrating alert\n9. screen saver')

    case '6':
        print ('1. Call settings\n2. Phone settings\n3. Security settings\n4. Restore factory settings')

    case '7':
        print ('You chose call divert')

    case '8':
        print ('You chose Games')

    case '9':
        print ('You chose Calculator')

    case '10':
	print('You chose Reminders')

    case '11':	
        print ('1. Alarm clock\n2. Clock settings\n3. Date settings\n4. Stop watch\n5. Countdown timer\n6. Auto update of date and time')

    case '12':
        print ('You chose profiles')

    case '13':
        print ('You chose sim services')

    
