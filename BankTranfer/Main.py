import pandas as pd
import Settings.config as cf
import src.tool as tool


def check(put):
    """

    :param put: zip obj contain index and values of columns
    :return: type of columns and list of bug(index)
    """
    data = tuple(put) # convert into tuple
    mail, m_index_bug = tool.check_mail(data)
    date, d_index_bug = tool.check_date(data)
    num, n_index_bug = tool.check_num(data)
    total_columns = len(data)
    if mail/(mail+len(m_index_bug)) >= 0.9:
        return "mail", m_index_bug
    if date/(date+len(d_index_bug)) >= 0.9:
        return "date", d_index_bug
    if num/(num+len(n_index_bug)) >= 0.9:
        return "number", n_index_bug
    return "text", []


if __name__ == "__main__":
    inp = pd.read_csv(cf.Ipath, dtype=str)
    for index in range(1, len(inp.columns)+1):
        res, bug = check(inp['No{}'.format(index)].items())
        print("Column No{} is {} value, has {} bugs, the index of each bug is:\n {}".format(index, res, len(bug), bug))
