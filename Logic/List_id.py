from Domain.Librarie import get_id


def list_id(vanzari):
    new_list = []
    for vanzare in vanzari:
        new_list.append(get_id(vanzare))
    return new_list