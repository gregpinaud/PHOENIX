#================================================================
#===================Create Gcode===========================
#================================================================
    
    
    
def export_gcl(model_name,panel_list,foam,hotwire):

    print(model_name)


    for ip, p in enumerate(panel_list):
        print("#    Panel nb "+str(ip+1))
        print(p.panel_span.strip('\n'))
        print(p.rootchord.strip('\n'))
    model_name,panel_list,foam,hotwire
    print("#    Foam ")
    for p in foam.param:
        print(p)
 
    print("#    Machine ")
    for p in hotwire.param:
        print(p)

    gc0 = []

    return gc0

def export_gcs(model_name,panel_list,foam,hotwire):
 

    gcl = export_gcl(model_name,panel_list,foam,hotwire)


    gcs = gcl

    return gcs


def export_gcls(model_name,panel_list,foam,hotwire):
 

    gcl = export_gcl(model_name,panel_list,foam,hotwire)

    gcs = gcl

    return [gcl,gcs]


