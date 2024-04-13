import React from 'react';
import { JsonLdProps } from './jsonld';
import type { ItemListElements } from 'src/types';
export interface ProfilePageJsonLdProps extends JsonLdProps {
    breadcrumb: string | ItemListElements[];
    lastReviewed?: string;
}
declare function ProfilePageJsonLd({ type, keyOverride, breadcrumb, ...rest }: ProfilePageJsonLdProps): React.JSX.Element;
export default ProfilePageJsonLd;
