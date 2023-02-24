from flask import Flask, request, jsonify
from flask.views import MethodView
from db import Announcement, Session

app = Flask('server')


class UserView(MethodView):

    def get(self, ann_id: int):
        with Session() as session:
            ann = session.query(Announcement).get(ann_id)

            return jsonify(
                {
                    'id': ann.id,
                    'header': ann.header,
                    'description': ann.description,
                    'creation_time': str(ann.creation_time.isoformat()),
                    'username': ann.username
                }
            )

    def post(self):
        json_data = request.json
        with Session() as session:
            new_ann = Announcement(**json_data)
            session.add(new_ann)
            session.commit()
            return jsonify(
                {
                    'id': new_ann.id,
                    'header': new_ann.header,
                    'created_at': str(new_ann.creation_time.isoformat())
                }
            )

    def patch(self, ann_id: int):
        json_data = request.json
        with Session() as session:
            ann = session.query(Announcement).get(ann_id)
            for field, value in json_data.items():
                setattr(ann, field, value)
            session.add(ann)
            session.commit()
            return jsonify(
                {
                    'id': ann.id,
                    'header': ann.header,
                    'description': ann.description,
                    'creation_time': str(ann.creation_time.isoformat()),
                    'username': ann.username
                }
            )


    def delete(self, ann_id: int):
        with Session() as session:
            ann = session.query(Announcement).get(ann_id)
            session.delete(ann)
            session.commit()
            return jsonify({"status": "deleted"})



app.add_url_rule('/announcements/<int:ann_id>', view_func=UserView.as_view('anns_with_id'), methods=['GET', 'PATCH', 'DELETE'])
app.add_url_rule('/announcements', view_func=UserView.as_view('anns'), methods=['POST'])
app.run(port=5000)
