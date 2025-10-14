import grade

def main():
    score_list = grade.readList()
    grade.processList(score_list)
    grade.writeList(score_list)

if __name__ == '__main__':
    main()