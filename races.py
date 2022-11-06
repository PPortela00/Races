from load_races import con
from tabulate import tabulate
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def menu():
    print('\n')
    print("[1] How many runners with more than 70 years of age have signed up in each type of event? (event, desc order count)")
    print("[2] How many runners are in each age class? (age_class, count)")
    print("[3] Which runner has more 1st places? (name, birthdate, count)")
    print("[4] What are the events with less then 42km distance? (event, year, distance)")
    print("[5] Chart for the percentage of the runners considering the Gender")
    print("[6] Chart for the Top 5 runners considering the maximum total distance ran")
    print("---------------------------5 Questions ---------------------------")
    print("[7] Who run the fastest 10K race ever (name, birthdate, time)")
    print("[8] What 10K race had the fastest average time (event, event date)?")
    print("[9] What teams had more than 3 participants in the 2016 maratona (team)?")
    print("[10] What are the 5 runners with more kilometers in total (name, birthdate, kms)?")
    print("[11] What was the best time improvement in two consecutive maratona races (name,birthdate, improvement)?")

    print("[0] Exit the program.")

menu()
option = int(input("Insert the command that you want to execute:\n"))

while option != 0:
    if option == 1:
        cur = con.cursor()
        cur.execute("""SELECT event, COUNT(*)
FROM runner JOIN classification ON r_id = runner_id
            JOIN event ON event_id = e_id
WHERE EXTRACT(YEAR FROM age(CURRENT_DATE, runner.b_date)) > 70
GROUP BY event
ORDER BY COUNT(*) DESC""")
        runners = cur.fetchall()
        from_db = []
        for runner in runners:
            result = list(runner)
            from_db.append(result)
        columns = ["Event", "No. of Old People Registrations"]
        df = pd.DataFrame(from_db, columns=columns)
        print(tabulate(df, headers='keys', showindex=False, tablefmt='orgtbl'))
    elif option == 2:
        cur = con.cursor()
        cur.execute("""SELECT age_class, COUNT(*)
FROM (SELECT DISTINCT r_id, age_class
      FROM classification JOIN runner ON runner_id = r_id
                          JOIN age_class ON class_id = a_id) AS age_classes
GROUP BY age_class""")
        runners = cur.fetchall()
        from_db = []
        for runner in runners:
            result = list(runner)
            from_db.append(result)
        columns = ["Age Class", "No. of Runners"]
        df = pd.DataFrame(from_db, columns=columns)
        print(tabulate(df, headers='keys', showindex=False, tablefmt='orgtbl'))
    elif option == 3:
        cur = con.cursor()
        cur.execute("""SELECT name, b_date, COUNT(*)
FROM classification JOIN runner ON runner_id = r_id
WHERE place = '1'
GROUP BY r_id
HAVING COUNT(*) >= ALL (SELECT COUNT(*)
                        FROM classification JOIN runner ON runner_id = r_id
                        WHERE place = '1'
                        GROUP BY r_id
                        ORDER BY COUNT(*) DESC
                        LIMIT 1)""")
        runners = cur.fetchall()
        from_db = []
        for runner in runners:
            result = list(runner)
            from_db.append(result)
        columns = ["Name", "Birth Date", "Nº of 1st Places"]
        df = pd.DataFrame(from_db, columns=columns)
        print(tabulate(df, headers='keys', showindex=False, tablefmt='orgtbl'))
    elif option == 4:
        cur = con.cursor()
        cur.execute("""SELECT DISTINCT event, distance.distance
FROM event JOIN distance ON event.distance = d_id
WHERE distance.distance < 42""")
        events = cur.fetchall()
        from_db = []
        for event in events:
            result = list(event)
            from_db.append(result)
        columns = ["Event", "Distance"]
        df = pd.DataFrame(from_db, columns=columns)
        print(tabulate(df, headers='keys', showindex=False, tablefmt='orgtbl'))
    elif option == 5:
        fig = plt.figure()
        ax = fig.add_subplot(111)
        cur = con.cursor()
        cur.execute('SELECT sex, COUNT(*) as count FROM runner JOIN sex ON runner.sex_id = sex.s_id GROUP BY sex')
        result = cur.fetchall()
        # print(result)
        ## the data

        sex = []
        count = []

        for i in result:
            sex.append(i[0])
            count.append(i[1])

        # colors
        colors = ['#FF0000', '#0000FF']

        # Pie Chart
        plt.pie(count, colors=colors, labels=sex,
                autopct='%1.1f%%', pctdistance=0.85)

        # draw circle
        centre_circle = plt.Circle((0, 0), 0.70, fc='white')
        fig = plt.gcf()

        # Adding Circle in Pie chart
        fig.gca().add_artist(centre_circle)

        # Adding Title of chart
        plt.title('Number of runners by gender')

        # Add Legends
        plt.legend(labels=sex, loc="upper right", title="sex")
        plt.show()
    elif option == 6:
        cur = con.cursor()
        cur.execute("""SELECT name, SUM(distance.distance) AS total_kms
                        FROM classification JOIN runner ON runner_id = r_id
                        JOIN event ON event_id = e_id JOIN distance ON event.distance = d_id
                        GROUP BY r_id
                        HAVING SUM(distance.distance) IN ( SELECT SUM(distance.distance)
                        FROM classification JOIN runner ON runner_id = r_id 
                        JOIN event ON event_id = e_id JOIN distance ON event.distance = d_id
                        GROUP BY r_id
                        ORDER BY SUM(distance.distance)
                        DESC LIMIT 5)
                        ORDER BY SUM(distance.distance) DESC""")
        result = cur.fetchall()

        name = []
        total_kms = []

        for i in result:
            name.append(i[0])
            total_kms.append(i[1])

        df = pd.DataFrame({'total_kms': total_kms}, index=name)

        # plot
        g = sns.catplot(kind='bar', data=df, x=name, y=total_kms, height=5, aspect=1.5)

        # iterate through the axes
        for ax in g.axes.flat:
            # annotate
            ax.bar_label(ax.containers[0], label_type='edge')

            # pad the spacing between the number and the edge of the figure; should be in the loop, otherwise only the last subplot would be adjusted
            ax.margins(y=0.1)

        plt.xlabel("Runner")
        plt.ylabel("Total kms")
        plt.title("TOP 5 runners")
        plt.xticks(rotation=0, horizontalalignment="center")
        plt.show()
    elif option == 7:
        cur = con.cursor()
        cur.execute("""SELECT name, b_date, MIN(o_time)
FROM classification JOIN event ON event_id = e_id
                    JOIN distance ON event.distance = d_id
                    JOIN runner ON runner_id = r_id
WHERE distance.distance = 10
GROUP BY r_id
HAVING MIN(o_time) <= ALL (SELECT MIN(o_time)
FROM classification JOIN event ON event_id = e_id
                    JOIN distance ON event.distance = d_id
                    JOIN runner ON runner_id = r_id
WHERE distance.distance = 10
GROUP BY r_id)""")
        runners = cur.fetchall()
        from_db = []
        for runner in runners:
            result = list(runner)
            from_db.append(result)
        columns = ["Name", "Birth Date", "Time"]
        df = pd.DataFrame(from_db, columns=columns)
        print(tabulate(df, headers='keys', showindex=False, tablefmt='orgtbl'))
    elif option == 8:
        cur = con.cursor()
        cur.execute("""SELECT event, e_year
FROM classification JOIN event ON event_id = e_id
                    JOIN distance ON event.distance = d_id
WHERE distance.distance = 10
GROUP BY e_id
HAVING AVG(o_time) <= ALL (SELECT AVG(o_time)
FROM classification JOIN event ON event_id = e_id
                    JOIN distance ON event.distance = d_id
WHERE distance.distance = 10
GROUP BY e_id)""")
        races = cur.fetchall()
        from_db = []
        for race in races:
            result = list(race)
            from_db.append(result)
        columns = ["Event", "Event Year"]
        df = pd.DataFrame(from_db, columns=columns)
        print(tabulate(df, headers='keys', showindex=False, tablefmt='orgtbl'))
    elif option == 9:
        cur = con.cursor()
        cur.execute("""SELECT team
FROM classification JOIN event ON event_id = e_id
WHERE e_year = 2016 AND event.event = 'maratona' AND team <> 'nan'
GROUP BY team
HAVING COUNT (*) > 3""")
        teams = cur.fetchall()
        from_db = []
        for team in teams:
            result = list(team)
            from_db.append(result)
        columns = ["Team"]
        df = pd.DataFrame(from_db, columns=columns)
        print(df)
    elif option == 10:
        cur = con.cursor()
        cur.execute("""SELECT name, b_date, SUM(distance.distance) AS total_kms
FROM classification JOIN runner ON runner_id = r_id
                    JOIN event ON event_id = e_id
                    JOIN distance on event.distance = d_id
GROUP BY r_id
HAVING SUM(distance.distance) IN (
SELECT SUM(distance.distance)
FROM classification JOIN runner ON runner_id = r_id
                    JOIN event ON event_id = e_id
                    JOIN distance on event.distance = d_id
GROUP BY r_id
ORDER BY SUM(distance.distance) DESC
LIMIT 5
)
ORDER BY SUM(distance.distance) DESC""")
        runners = cur.fetchall()
        from_db = []
        for runner in runners:
            result = list(runner)
            from_db.append(result)
        columns = ["Name", "Birth Date", "Total KM´s"]
        df = pd.DataFrame(from_db, columns=columns)
        print(tabulate(df, headers='keys', showindex=False, tablefmt='orgtbl'))
    elif option == 11:
        cur = con.cursor()
        cur.execute("""SELECT name, b_date, GREATEST(dif_1213, dif_1314, dif_1415, dif_1516) AS improvement
FROM (

SELECT name, b_date, o_time_2012 - o_time_2013 AS dif_1213, o_time_2013 - o_time_2014 AS dif_1314, o_time_2014 - o_time_2015 AS dif_1415, o_time_2015 - o_time_2016 AS dif_1516
FROM (SELECT name, b_date, o_time AS o_time_2012, e_year
      FROM classification JOIN event ON event_id = e_id
                    JOIN runner ON runner_id = r_id
      WHERE event.event = 'maratona'
      GROUP BY r_id, o_time, e_year
      HAVING e_year = 2012) AS year_2012 
FULL OUTER JOIN (SELECT name, b_date, o_time AS o_time_2013, e_year
      FROM classification JOIN event ON event_id = e_id
                          JOIN runner ON runner_id = r_id
      WHERE event.event = 'maratona'
      GROUP BY r_id, o_time, e_year
      HAVING e_year = 2013) AS year_2013 USING(name, b_date)
FULL OUTER JOIN (SELECT name, b_date, o_time AS o_time_2014, e_year
      FROM classification JOIN event ON event_id = e_id
                          JOIN runner ON runner_id = r_id
      WHERE event.event = 'maratona'
      GROUP BY r_id, o_time, e_year
      HAVING e_year = 2014) AS year_2014 USING(name, b_date)
FULL OUTER JOIN (SELECT name, b_date, o_time AS o_time_2015, e_year
      FROM classification JOIN event ON event_id = e_id
                          JOIN runner ON runner_id = r_id
      WHERE event.event = 'maratona'
      GROUP BY r_id, o_time, e_year
      HAVING e_year = 2015) AS year_2015 USING(name, b_date)
FULL OUTER JOIN (SELECT name, b_date, o_time AS o_time_2016, e_year
      FROM classification JOIN event ON event_id = e_id
                          JOIN runner ON runner_id = r_id
      WHERE event.event = 'maratona'
      GROUP BY r_id, o_time, e_year
      HAVING e_year = 2016) AS year_2016 USING(name, b_date)

) AS differences

GROUP BY name, b_date, improvement

HAVING GREATEST(dif_1213, dif_1314, dif_1415, dif_1516) IS NOT NULL

ORDER BY GREATEST(dif_1213, dif_1314, dif_1415, dif_1516) DESC

LIMIT 1
""")
        improvements = cur.fetchall()
        from_db = []
        for improvement in improvements:
            result = list(improvement)
            from_db.append(result)
        columns = ["Name", "Birth Date", "Improvement"]
        df = pd.DataFrame(from_db, columns=columns)
        print(tabulate(df, headers='keys', showindex=False, tablefmt='orgtbl'))
    else:
        print("Invalid Option")

    print("\n")
    menu()
    option = int(input("Insert the command that you want to execute:"))

print("\n")
print("Thanks for using this program. See you soon")