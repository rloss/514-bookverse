-- 1. User
CREATE TABLE User (
  id UUID PRIMARY KEY,
  username VARCHAR NOT NULL,
  email VARCHAR UNIQUE NOT NULL,
  hashed_password VARCHAR NOT NULL,
  created_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP NOT NULL
);

-- 2. SocialAccount
CREATE TABLE SocialAccount (
  id UUID PRIMARY KEY,
  user_id UUID REFERENCES User(id) ON DELETE CASCADE,
  provider VARCHAR CHECK (provider IN ('google', 'kakao', 'github', 'naver')) NOT NULL,
  provider_user_id VARCHAR NOT NULL,
  email VARCHAR,
  username VARCHAR,
  profile_image_url VARCHAR,
  created_at TIMESTAMP NOT NULL,
  UNIQUE (provider, provider_user_id)
);

-- 3. UserProfile
CREATE TABLE UserProfile (
  id UUID PRIMARY KEY,
  user_id UUID UNIQUE REFERENCES User(id) ON DELETE CASCADE,
  bio TEXT,
  profile_image_url VARCHAR,
  website_url VARCHAR,
  location VARCHAR,
  created_at TIMESTAMP NOT NULL
);

-- 4. Group
CREATE TABLE Group (
  id UUID PRIMARY KEY,
  name VARCHAR NOT NULL,
  description TEXT,
  cover_image_url VARCHAR,
  owner_id UUID REFERENCES User(id) ON DELETE SET NULL,
  created_at TIMESTAMP NOT NULL
);

-- 5. GroupUser
CREATE TABLE GroupUser (
  id UUID PRIMARY KEY,
  group_id UUID REFERENCES Group(id) ON DELETE CASCADE,
  user_id UUID REFERENCES User(id) ON DELETE CASCADE,
  role VARCHAR CHECK (role IN ('owner', 'admin', 'member')) NOT NULL,
  status VARCHAR CHECK (status IN ('active', 'pending', 'banned')) NOT NULL,
  joined_at TIMESTAMP NOT NULL,
  UNIQUE (group_id, user_id)
);

-- 6. Book
CREATE TABLE Book (
  id UUID PRIMARY KEY,
  title VARCHAR NOT NULL,
  author VARCHAR NOT NULL,
  publisher VARCHAR,
  published_date DATE,
  description TEXT,
  isbn VARCHAR,
  image_url VARCHAR
);

-- 7. Post
CREATE TABLE Post (
  id UUID PRIMARY KEY,
  author_id UUID REFERENCES User(id) ON DELETE SET NULL,
  group_id UUID REFERENCES Group(id) ON DELETE SET NULL,
  activity_id UUID REFERENCES GroupActivity(id) ON DELETE SET NULL,
  category VARCHAR CHECK (category IN ('review', 'announcement', 'community')) NOT NULL,
  visibility VARCHAR CHECK (visibility IN ('public', 'group-only', 'private')) NOT NULL,
  title VARCHAR NOT NULL,
  content TEXT NOT NULL,
  created_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP NOT NULL
);

-- 8. PostBook
CREATE TABLE PostBook (
  id UUID PRIMARY KEY,
  post_id UUID REFERENCES Post(id) ON DELETE CASCADE,
  book_id UUID REFERENCES Book(id) ON DELETE CASCADE,
  note TEXT,
  is_primary BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMP NOT NULL,
  UNIQUE (post_id, book_id)
);

-- 9. Comment
CREATE TABLE Comment (
  id UUID PRIMARY KEY,
  post_id UUID REFERENCES Post(id) ON DELETE CASCADE,
  author_id UUID REFERENCES User(id) ON DELETE SET NULL,
  content TEXT NOT NULL,
  created_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP NOT NULL
);

-- 10. GroupActivity
CREATE TABLE GroupActivity (
  id UUID PRIMARY KEY,
  group_id UUID REFERENCES Group(id) ON DELETE CASCADE,
  type VARCHAR CHECK (type IN ('shared-reading', 'discussion', 'challenge')) NOT NULL,
  title VARCHAR NOT NULL,
  description TEXT,
  start_at TIMESTAMP,
  end_at TIMESTAMP,
  created_by UUID REFERENCES User(id) ON DELETE SET NULL,
  status VARCHAR CHECK (status IN ('planned', 'active', 'completed')) NOT NULL,
  created_at TIMESTAMP NOT NULL
);

-- 11. GroupActivityBook
CREATE TABLE GroupActivityBook (
  id UUID PRIMARY KEY,
  activity_id UUID REFERENCES GroupActivity(id) ON DELETE CASCADE,
  book_id UUID REFERENCES Book(id) ON DELETE CASCADE,
  selected BOOLEAN DEFAULT FALSE,
  UNIQUE (activity_id, book_id)
);

-- 12. GroupActivityPost
CREATE TABLE GroupActivityPost (
  id UUID PRIMARY KEY,
  activity_id UUID REFERENCES GroupActivity(id) ON DELETE CASCADE,
  post_id UUID REFERENCES Post(id) ON DELETE CASCADE,
  book_id UUID REFERENCES Book(id) ON DELETE SET NULL,
  submitted_at TIMESTAMP NOT NULL,
  participation_style VARCHAR,
  UNIQUE (activity_id, post_id)
);

-- 13. Schedule
CREATE TABLE Schedule (
  id UUID PRIMARY KEY,
  group_id UUID REFERENCES Group(id) ON DELETE CASCADE,
  activity_id UUID REFERENCES GroupActivity(id) ON DELETE SET NULL,
  title VARCHAR NOT NULL,
  description TEXT,
  scheduled_date DATE NOT NULL,
  created_by UUID REFERENCES User(id) ON DELETE SET NULL,
  created_at TIMESTAMP NOT NULL
);

-- 14. GroupActivitySchedule
CREATE TABLE GroupActivitySchedule (
  id UUID PRIMARY KEY,
  activity_id UUID REFERENCES GroupActivity(id) ON DELETE CASCADE,
  schedule_id UUID REFERENCES Schedule(id) ON DELETE CASCADE,
  UNIQUE (activity_id, schedule_id)
);
