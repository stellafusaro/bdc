#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 11:59:46 2023

@author: stellafusaro

A program that helps user search for Broadway Dance Center (BDC) dance class using either the teaher or the day
of the week in which they would like to take the class. 

"""

import requests
from bs4 import BeautifulSoup


url = 'https://broadwaydancecenter.com/schedule/schedule-by-discipline'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

#Find all dance styles offered by BDC and compare them to the styles the user inputs they want to take.

danceStyles = soup.find_all('h3', class_='bdc-subtitle')
Style = input("What style dance class would you like to take? ")

selectedStyle = None
for styles in danceStyles:
    if(Style == styles.text.strip()):
        selectedStyle = styles.text
        break
    
#This block starts if the style the person selected is a main style offered by BDC

if(selectedStyle):
    
    print("The style you selected was registered.")
    
    #This block starts if the style the user selected is Ballet
    
    if(selectedStyle == "Ballet"):
        num = input("Do you have a teacher preference(1) or a Day preference (2)? ")
        balletSection = soup.find(id = "block-views-0115937599a1faadf675c7e52f2e3eab")
    
        #If the user has a teacher preference.
        if(num == "1"):
            
            
            if(balletSection): 
                
                teachers = balletSection.find_all('h3', class_ = 'bdc-tout-title')
                print("Teachers for", Style)
                number = 0
                
                #List all teachers found on BDC website for Ballet.
    
                for teacher in teachers:
                    print(number, ". " , teacher.text)
                    number += 1
                    
                teacherChoice = input("Which teacher would you prefer (select number)?")
                
                #Finds the class times for each teacher.
                theTeachers = balletSection.find_all(class_= 'bdc-tout-tagline-sm')
                teacherChoiceNumber = int(teacherChoice)
                index_to_print = teacherChoiceNumber
                
                #Prints the class times for desired teacher
                if 0 <= index_to_print < len(theTeachers):
                    element = theTeachers[index_to_print]
                    print(element.text)
                else:
                    print("Index out of range.")
                    
        #If the user would rather find class by day of the week             
        elif(num == "2"):
            
            if(balletSection): 
                day = input("What day of the week would you like to take your class? (select number) \n 1. Sunday \n 2. Monday \n 3. Tuesday \n 4. Wednesday \n 5. Thursday \n 6. Friday \n 7. Saturday \n")
                
                daySearcher = balletSection.find_all(class_= 'bdc-tout-tagline-sm')
                
                #Finds the classes on the day selected by the user.
                for element in daySearcher:
                    br_tags = element.find_all("br")
                    for br in br_tags:
                        next_sibling = br.next_sibling
                        if next_sibling and isinstance(next_sibling, str):
                            if(day == "1" and "Sun" in next_sibling): 
                                print(next_sibling.strip())
                            if(day == "2" and "Mon" in next_sibling): 
                                print(next_sibling.strip())
                            if(day == "3" and "Tue" in next_sibling): 
                                print(next_sibling.strip())
                            if(day == "4" and "Wed" in next_sibling): 
                                print(next_sibling.strip())
                            if(day == "5" and "Thu" in next_sibling): 
                                print(next_sibling.strip())
                            if(day == "6" and "Fri" in next_sibling): 
                                print(next_sibling.strip())
                            if(day == "7" and "Sat" in next_sibling): 
                                print(next_sibling.strip())
        else:
            print("Error")
                
        
    #This block starts if the style the user selected is Contemporary                
    if(selectedStyle == "Contemporary"):
            num = input("Do you have a teacher preference(1) or a Day preference (2)? ")
            contemporarySection = soup.find(id = "block-views-48e08263a54e142875b26f82ce302d3c")
    
            #If the user has a teacher preference.
            if(num == "1"):
            
                if(contemporarySection): 
                    teachers = contemporarySection.find_all('h3', class_ = 'bdc-tout-title')
                    print("Teachers for", Style)
                    number = 0
                    
                    #Lists all teachers found on BDC website for Contemporary.
                    for teacher in teachers:
                        print(number, ". " , teacher.text)
                        number += 1
                    
                    teacherChoice = input("Which teacher would you prefer (select number)?")
                
                    #Finds the class times for each teacher.
                    theTeachers = contemporarySection.find_all(class_= 'bdc-tout-tagline-sm')
                    teacherChoiceNumber = int(teacherChoice)
                    index_to_print = teacherChoiceNumber

                    #Prints the class times for the desired teacher.
                    if 0 <= index_to_print < len(theTeachers):
                        element = theTeachers[index_to_print]
                        print(element.text)
                    else:
                            print("Index out of range.")
            
            #If the user would rather find class by day of the week.
            elif(num == "2"):
            
                if(contemporarySection): 
                    day = input("What day of the week would you like to take your class? (select number) \n 1. Sunday \n 2. Monday \n 3. Tuesday \n 4. Wednesday \n 5. Thursday \n 6. Friday \n 7. Saturday \n")
                
                    daySearcher = contemporarySection.find_all(class_= 'bdc-tout-tagline-sm')
                
                    #Finds the classes on the day selected by user.
                    for element in daySearcher:
                        br_tags = element.find_all("br")
                        for br in br_tags:
                            next_sibling = br.next_sibling
                            if next_sibling and isinstance(next_sibling, str):
                                if(day == "1" and "Sun" in next_sibling): 
                                    print(next_sibling.strip())
                                if(day == "2" and "Mon" in next_sibling): 
                                    print(next_sibling.strip())
                                if(day == "3" and "Tue" in next_sibling): 
                                    print(next_sibling.strip())
                                if(day == "4" and "Wed" in next_sibling): 
                                    print(next_sibling.strip())
                                if(day == "5" and "Thu" in next_sibling): 
                                    print(next_sibling.strip())
                                if(day == "6" and "Fri" in next_sibling): 
                                    print(next_sibling.strip())
                                if(day == "7" and "Sat" in next_sibling): 
                                    print(next_sibling.strip())
            else:
                print("Error")
    
    #This block starts if the style the user selected is Hip-Hop / Street Styles
    if(selectedStyle == "Hip-Hop / Street Styles"):
        num = input("Do you have a teacher preference(1) or a Day preference (2)? ")
        HHSection = soup.find(id = "block-views-19d01c4e2209e1fb00aa6cbca042381f")
    
        #If the user has a teacher preference.
        if(num == "1"):
            
            if(HHSection): 
                
                teachers = HHSection.find_all('h3', class_ = 'bdc-tout-title')
                print("Teachers for", Style)
                number = 0
                
                
                #Lists all Hip-Hop and Street Styles teachers of BDC website.
                for teacher in teachers:
                    print(number, ". " , teacher.text)
                    number += 1
                    
                teacherChoice = input("Which teacher would you prefer (select number)?")
                
                #Finds the class times for each teacher.
                theTeachers = HHSection.find_all(class_= 'bdc-tout-tagline-sm')
                teacherChoiceNumber = int(teacherChoice)
                index_to_print = teacherChoiceNumber

                #Prints the class times for desired teacher. 
                if 0 <= index_to_print < len(theTeachers):
                    element = theTeachers[index_to_print]
                    print(element.text)
                else:
                    print("Index out of range.")
        
        #If the user would rather find class by day of the week.
        elif(num == "2"):
            
            if(HHSection): 
                day = input("What day of the week would you like to take your class? (select number) \n 1. Sunday \n 2. Monday \n 3. Tuesday \n 4. Wednesday \n 5. Thursday \n 6. Friday \n 7. Saturday \n")
                
                daySearcher = HHSection.find_all(class_= 'bdc-tout-tagline-sm')
                
                #Finds the classes on the day selected by user.
                for element in daySearcher:
                    br_tags = element.find_all("br")
                    for br in br_tags:
                        next_sibling = br.next_sibling
                        if next_sibling and isinstance(next_sibling, str):
                            if(day == "1" and "Sun" in next_sibling): 
                                print(next_sibling.strip())
                            if(day == "2" and "Mon" in next_sibling): 
                                print(next_sibling.strip())
                            if(day == "3" and "Tue" in next_sibling): 
                                print(next_sibling.strip())
                            if(day == "4" and "Wed" in next_sibling): 
                                print(next_sibling.strip())
                            if(day == "5" and "Thu" in next_sibling): 
                                print(next_sibling.strip())
                            if(day == "6" and "Fri" in next_sibling): 
                                print(next_sibling.strip())
                            if(day == "7" and "Sat" in next_sibling): 
                                print(next_sibling.strip())
        else:
            print("Error")
    
    #This block starts if the style the user selected is Jazz                
    if(selectedStyle == "Jazz"):
        num = input("Do you have a teacher preference(1) or a Day preference (2)? ")
        jazzSection = soup.find(id = "block-views-84433964bdf00d95cfcb85bad3caeee3")
    
        #If the user has a teacher preference. 
        if(num == "1"):
                     
            if(jazzSection): 
                
                teachers = jazzSection.find_all('h3', class_ = 'bdc-tout-title')
                print("Teachers for", Style)
                number = 0
                
                #Lists all Jazz teachers found on BDC wwebsite. 
                for teacher in teachers:
                    print(number, ". " , teacher.text)
                    number += 1
                    
                teacherChoice = input("Which teacher would you prefer (select number)?")
                
                #Finds the class times for each teacher. 
                theTeachers = jazzSection.find_all(class_= 'bdc-tout-tagline-sm')
                teacherChoiceNumber = int(teacherChoice)
                index_to_print = teacherChoiceNumber

                #Prints the class times for desired teacher.
                if 0 <= index_to_print < len(theTeachers):
                    element = theTeachers[index_to_print]
                    print(element.text)
                else:
                    print("Index out of range.")
        
        #If the user would rather find class by day of the week.
        elif(num == "2"):
            
            if(jazzSection): 
                day = input("What day of the week would you like to take your class? (select number) \n 1. Sunday \n 2. Monday \n 3. Tuesday \n 4. Wednesday \n 5. Thursday \n 6. Friday \n 7. Saturday \n")
                
                daySearcher = jazzSection.find_all(class_= 'bdc-tout-tagline-sm')
                
                #Finds the classes on the day selected by user.
                for element in daySearcher:
                    br_tags = element.find_all("br")
                    for br in br_tags:
                        next_sibling = br.next_sibling
                        if next_sibling and isinstance(next_sibling, str):
                            if(day == "1" and "Sun" in next_sibling): 
                                print(next_sibling.strip())
                            if(day == "2" and "Mon" in next_sibling): 
                                print(next_sibling.strip())
                            if(day == "3" and "Tue" in next_sibling): 
                                print(next_sibling.strip())
                            if(day == "4" and "Wed" in next_sibling): 
                                print(next_sibling.strip())
                            if(day == "5" and "Thu" in next_sibling): 
                                print(next_sibling.strip())
                            if(day == "6" and "Fri" in next_sibling): 
                                print(next_sibling.strip())
                            if(day == "7" and "Sat" in next_sibling): 
                                print(next_sibling.strip())
        else:
            print("Error")
            
            
    #This block starts if the style the user selected is Tap.
    if(selectedStyle == "Tap"):
        num = input("Do you have a teacher preference(1) or a Day preference (2)? ")
        tapSection = soup.find(id = "block-views-96097a9e5e254d29ecf8a474bfd79a5b")
    
        #If the user has a teacher preference. 
        if(num == "1"):
            
            
            if(tapSection): 
                teachers = tapSection.find_all('h3', class_ = 'bdc-tout-title')
                print("Teachers for", Style)
                number = 0
                
                
                #List all Tap teachers found on BDC website. 
                for teacher in teachers:
                    print(number, ". " , teacher.text)
                    number += 1
                    
                teacherChoice = input("Which teacher would you prefer (select number)?")
                
                #Finds class times for each teacher.
                theTeachers = tapSection.find_all(class_= 'bdc-tout-tagline-sm')
                teacherChoiceNumber = int(teacherChoice)
                index_to_print = teacherChoiceNumber

                #Prints the class time for desired teacher.
                if 0 <= index_to_print < len(theTeachers):
                    element = theTeachers[index_to_print]
                    print(element.text)
                else:
                    print("Index out of range.") 
                    
        #If the user would rather find class by day of the week.
        elif(num == "2"):
            
            if(tapSection): 
                day = input("What day of the week would you like to take your class? (select number) \n 1. Sunday \n 2. Monday \n 3. Tuesday \n 4. Wednesday \n 5. Thursday \n 6. Friday \n 7. Saturday \n")
                
                daySearcher = tapSection.find_all(class_= 'bdc-tout-tagline-sm')
                
                #Finds the classes on the day selected by user.
                for element in daySearcher:
                    br_tags = element.find_all("br")
                    for br in br_tags:
                        next_sibling = br.next_sibling
                        if next_sibling and isinstance(next_sibling, str):
                            if(day == "1" and "Sun" in next_sibling): 
                                print(next_sibling.strip())
                            if(day == "2" and "Mon" in next_sibling): 
                                print(next_sibling.strip())
                            if(day == "3" and "Tue" in next_sibling): 
                                print(next_sibling.strip())
                            if(day == "4" and "Wed" in next_sibling): 
                                print(next_sibling.strip())
                            if(day == "5" and "Thu" in next_sibling): 
                                print(next_sibling.strip())
                            if(day == "6" and "Fri" in next_sibling): 
                                print(next_sibling.strip())
                            if(day == "7" and "Sat" in next_sibling): 
                                print(next_sibling.strip())
        else:
            print("Error")
    
    #This block starts if the style the user selected is Theater                
    if(selectedStyle == "Theater"):
        num = input("Do you have a teacher preference(1) or a Day preference (2)? ")
        theaterSection = soup.find(id = "block-views-4fb57bf3b5f66c2fd761dc458c6a7d4a")
    
        #If the user has a teacher preference. 
        if(num == "1"):
            
            
            if(theaterSection): 
                
                teachers = theaterSection.find_all('h3', class_ = 'bdc-tout-title')
                print("Teachers for", Style)
                number = 0
                
                #List all Theater teachers found on BDC website.
                for teacher in teachers:
                    print(number, ". " , teacher.text)
                    number += 1
                    
                teacherChoice = input("Which teacher would you prefer (select number)?")
                
                #Finds the class times for each teacher.
                theTeachers = theaterSection.find_all(class_= 'bdc-tout-tagline-sm')
                teacherChoiceNumber = int(teacherChoice)
                index_to_print = teacherChoiceNumber

                #Prints the class times for desired teachers.
                if 0 <= index_to_print < len(theTeachers):
                    element = theTeachers[index_to_print]
                    print(element.text)
                else:
                    print("Index out of range.")
                    
        #If the user would rather find class by day of the week.
        elif(num == "2"):
            
            if(theaterSection): 
                day = input("What day of the week would you like to take your class? (select number) \n 1. Sunday \n 2. Monday \n 3. Tuesday \n 4. Wednesday \n 5. Thursday \n 6. Friday \n 7. Saturday \n")
                
                daySearcher = theaterSection.find_all(class_= 'bdc-tout-tagline-sm')
                
                #Finds the classes on the day selected by user.
                for element in daySearcher:
                    br_tags = element.find_all("br")
                    for br in br_tags:
                        next_sibling = br.next_sibling
                        if next_sibling and isinstance(next_sibling, str):
                            if(day == "1" and "Sun" in next_sibling): 
                                print(next_sibling.strip())
                            if(day == "2" and "Mon" in next_sibling): 
                                print(next_sibling.strip())
                            if(day == "3" and "Tue" in next_sibling): 
                                print(next_sibling.strip())
                            if(day == "4" and "Wed" in next_sibling): 
                                print(next_sibling.strip())
                            if(day == "5" and "Thu" in next_sibling): 
                                print(next_sibling.strip())
                            if(day == "6" and "Fri" in next_sibling): 
                                print(next_sibling.strip())
                            if(day == "7" and "Sat" in next_sibling): 
                                print(next_sibling.strip())
        else:
            print("Error")
                    
         
#If the styles is not registered as a main style offered by BDC.
else:
    
    print("The style you listed is not one of the main styles offered. Continue for other styles.")
    num = input("Do you have a teacher preference(1) or a Day preference (2)? ")
    otherSection = soup.find(id = "block-views-f7fc327f448f4c9fb5ab130da6ddd347")
    
    #If the user has a teacher preference
    if(num == "1"):
        
        if(otherSection): 
            teachers = otherSection.find_all('h3', class_ = 'bdc-tout-title')
            print("Teachers for", Style)
            number = 0
            
            #List all alternative teachers found on BDC website.
            for teacher in teachers:
                print(number, ". " , teacher.text)
                number += 1
                    
            teacherChoice = input("Which teacher would you prefer (select number)?")
                
            #Finds the class time for each teacher.
            theTeachers = otherSection.find_all(class_= 'bdc-tout-tagline-sm')
            teacherChoiceNumber = int(teacherChoice)
            index_to_print = teacherChoiceNumber

            #Prints the class time for desired teacher.
            if 0 <= index_to_print < len(theTeachers):
                element = theTeachers[index_to_print]
                print(element.text)
            else:
                print("Index out of range.")
                
    #If the user would rather find class by day of the week.
    elif(num == "2"):
        
        if(otherSection): 
            day = input("What day of the week would you like to take your class? (select number) \n 1. Sunday \n 2. Monday \n 3. Tuesday \n 4. Wednesday \n 5. Thursday \n 6. Friday \n 7. Saturday \n")
            
            daySearcher = otherSection.find_all(class_= 'bdc-tout-tagline-sm')
            
            #Finds the classes on the day selected by user.
            for element in daySearcher:
                br_tags = element.find_all("br")
                for br in br_tags:
                    next_sibling = br.next_sibling
                    if next_sibling and isinstance(next_sibling, str):
                        if(day == "1" and "Sun" in next_sibling): 
                            print(next_sibling.strip())
                        if(day == "2" and "Mon" in next_sibling): 
                            print(next_sibling.strip())
                        if(day == "3" and "Tue" in next_sibling): 
                            print(next_sibling.strip())
                        if(day == "4" and "Wed" in next_sibling): 
                            print(next_sibling.strip())
                        if(day == "5" and "Thu" in next_sibling): 
                            print(next_sibling.strip())
                        if(day == "6" and "Fri" in next_sibling): 
                            print(next_sibling.strip())
                        if(day == "7" and "Sat" in next_sibling): 
                            print(next_sibling.strip())
    else:
        print("Error")
 
